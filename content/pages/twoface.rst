apw/twoface
###########

:url: twoface
:save_as: twoface.html

This page contains catalogs and data products from our search for binary star
systems using data release 14 (`DR14
<http://www.sdss.org/dr14/irspec/spectro_data/>`_) of the `APOGEE
<http://www.sdss.org/surveys/apogee-2/>`_ survey.

All code related to this project can be found in `this GitHub repository
<https://github.com/adrn/twoface>`_.

Catalogs
========

Derived parameters
------------------

If you're just looking for catalogs of binaries, these are probably the files
you want.

* `Orbital parameters for uniquely-determined binaries
  <https://s3.amazonaws.com/apogee-twoface/highK-unimodal.fits>`_ (320 stars)

  This file contains maximum *a posteriori* values of the orbital parameters for
  320 systems that were flagged as having unimodal posterior samplings. The
  uncertainties on the orbital parameters (`_err` columns) are estimated using
  percentiles from the 1D (marginal) distributions: Note that the parameters
  often have correlated posterior distributions, so if this matters to your
  analysis, you should directly use the posterior samples provided below
  (especially the MCMC samplings file). To select out a clean sample of systems
  with orbital solutions that have been visually inspected, and with converged
  MCMC samplings in Python, use::

    from astropy.table import QTable
    tbl = QTable.read('highK-unimodal.fits',
                      astropy_native=True, character_as_bytes=False)
    clean = tbl[(tbl['clean_flag'] == 0) & tbl['converged']]

  This file also contains all columns from the APOGEE DR14 allStar file, and
  columns from Melissa Ness' derived masses and ages from `this paper
  <https://ui.adsabs.harvard.edu/#abs/2016ApJ...823..114N/abstract>`_ (where
  available).

* `Orbital parameters for binaries with bimodal samplings
  <https://s3.amazonaws.com/apogee-twoface/highK-bimodal.fits>`_ (106 stars)

  This table contains two rows per system for all systems with bimodal posterior
  samplings over orbital period. Within each mode, the maximum *a posteriori*
  sample is reported.

* `1st percentiles computed from all posterior samplings of the velocity
  semi-amplitude, *K*
  <https://s3.amazonaws.com/apogee-twoface/lnK-percentiles.fits>`_ (96,231 stars)

  This file contains the 1st percentile of the velocity semi-amplitude, *K*,
  samplings for all APOGEE stars in our parent sample. You can use this value to
  select probable binaries: systems with a large value of this parameter have
  large radial velocity variations that can be explained by two-body orbital
  moton.

Raw catalogs
------------

* `All posterior samplings returned by *The Joker* <https://s3.amazonaws.com/apogee-twoface/apogee-jitter.hdf5>`_ (96,231 stars)
* `Database containing metadata for APOGEE DR14 stars <https://s3.amazonaws.com/apogee-twoface/apogee.sqlite>`_ (96,231 stars)
* `MCMC samplings for stars with unimodal samplings <https://s3.amazonaws.com/apogee-twoface/apogee-jitter-mcmc.hdf5>`_ (320 stars)
* `All posterior samplings for the (simulated) control sample <https://s3.amazonaws.com/apogee-twoface/apogee-jitter-control.hdf5>`_ (16,384 stars)
