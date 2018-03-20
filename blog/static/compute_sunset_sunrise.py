# Standard library
import datetime

# Third-party
import astropy.units as u
import astropy.coordinates as coord
from astropy.time import Time
import h5py
import numpy as np
import pytz
from scipy.signal import argrelmin
import pandas as pd
from timezonefinder import TimezoneFinder

tzf = TimezoneFinder()


class SunComputer:

    def __init__(self, us_counties_file, cache_file, n_time=512):
        county = pd.read_csv(us_counties_file, delimiter='\t')
        tz_names = [tzf.timezone_at(lat=r['INTPTLAT'], lng=r['INTPTLONG'])
                    for i, r in county.iterrows()]
        self.tzs = np.array([pytz.timezone(tz) for tz in tz_names])
        self.county_locs = coord.EarthLocation(lon=county['INTPTLONG']*u.deg,
                                               lat=county['INTPTLAT']*u.deg)
        self.n_time = n_time
        self.cache_file = cache_file

    def get_times(self, day):
        """Estimate the local time of sunset and sunrise at the specified
        locations on the specified date.

        Parameters
        ----------
        day : `astropy.time.Time`
            The UTC day to compute sunset on.
        """

        print(day)

        # UTC timezone used below to convert to local time
        utc = pytz.timezone('UTC')

        # Generate a grid of times to use to search for sunset:
        time_grid = day + np.linspace(0, 24, self.n_time) * u.hour

        # Get the Sun's position at all of the (UTC) times:
        sun = coord.get_sun(time_grid[:, None])

        # Create a 2D grid of AltAz frames given the locations
        # and times, then compute the Sun's local altitude and azimuth
        # at each of those frames:
        altaz_frame = coord.AltAz(location=self.county_locs[None],
                                  obstime=time_grid[:, None])
        sun_altaz = sun.transform_to(altaz_frame)

        # Find the indices of all minima in the sun altitude^2 -- there
        # should be 2: close to sunset, and close to sunrise:
        min_idx = np.array([argrelmin(a**2, axis=0, mode='clip')[0]
                            for a in sun_altaz.alt.degree.T])

        # Now, figure out which of the two sun altitude minima is sunset
        # by computing the derivative of altitude w.r.t. time:
        sunset_idx = []
        sunrise_idx = []
        for i, idx in enumerate(min_idx):
            alt = sun_altaz.alt.degree
            try:
                sunset_idx.append(idx[np.array([alt[min(j+1, len(alt)-1), i] -
                                                alt[max(j-1, 0), i]
                                                for j in idx]) < 0][0])
            except IndexError:
                sunset_idx.append(0)
                continue

            try:
                sunrise_idx.append(idx[np.array([alt[min(j+1, len(alt)-1), i] -
                                                 alt[max(j-1, 0), i]
                                                 for j in idx]) > 0][0])
            except IndexError:
                sunrise_idx.append(0)
                continue

        sunset_idx = np.array(sunset_idx)
        sunrise_idx = np.array(sunrise_idx)

        # Convert the UTC sunset time estimates to local times. Here we
        # assume that the time sampling is dense enough that the time of
        # min(alt**2) is close enough to the actual sunset:
        sun_time = sun_altaz.obstime.datetime
        sunset = np.array([utc.localize(sun_time[j, i]).astimezone(self.tzs[i])
                           for i, j in enumerate(sunset_idx)])
        sunrise = np.array([utc.localize(sun_time[j, i]).astimezone(self.tzs[i])
                            for i, j in enumerate(sunrise_idx)])

        sunset_hours = np.array([s.hour + s.minute/60 + s.second/3600
                                 for s in sunset])
        sunrise_hours = np.array([s.hour + s.minute/60 + s.second/3600
                                  for s in sunrise])

        return sunset_hours, sunrise_hours

    def __call__(self, task):
        day = Time(task)
        return day.datetime.strftime('%Y-%m-%d'), self.get_times(day)

    def callback(self, result):
        date, (sunset_hours, sunrise_hours) = result
        with h5py.File(self.cache_file) as f:
            if date not in f:
                g = f.create_group(date)
                g.create_dataset('sunset_hours', data=sunset_hours)
                g.create_dataset('sunrise_hours', data=sunrise_hours)


def main(pool):

    all_days = Time('2017-12-21') + np.arange(0, 365+0.1, 1)*u.day
    sc = SunComputer('US-counties.txt',
                     cache_file='sunrise_sunset.hdf5',
                     n_time=1024)

    tasks = [t.datetime.strftime('%Y-%m-%d') for t in all_days]
    for r in pool.map(sc, tasks, callback=sc.callback):
        pass

    pool.close()


if __name__ == "__main__":
    from argparse import ArgumentParser
    from schwimmbad import choose_pool

    # Define parser object
    parser = ArgumentParser(description="")

    group = parser.add_mutually_exclusive_group()
    group.add_argument("--procs", dest="n_procs", default=1,
                       type=int, help="Number of processes.")
    group.add_argument("--mpi", dest="mpi", default=False,
                       action="store_true", help="Run with MPI.")

    args = parser.parse_args()

    pool_kwargs = dict(mpi=args.mpi, processes=args.n_procs)
    pool = choose_pool(**pool_kwargs)

    main(pool=pool)
