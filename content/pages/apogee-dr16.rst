apw/APOGEE-DR16
###############

:url: apogee-dr16
:save_as: apogee-dr16.html

This page contains catalogs and data products from our search for binary star
systems using data release 16 (`DR16
<http://www.sdss.org/dr16/irspec/spectro_data/>`_) of the `APOGEE
<http://www.sdss.org/surveys/apogee-2/>`_ surveys.
The generation of these catalogs and some initial results are described in
`Price-Whelan et al. 2020 <https://arxiv.org/abs/2002.XXXXX>`_ (PW20).

All code related to this project can be found in `this GitHub repository
<https://github.com/adrn/hq>`_.

Catalogs
========

* `Orbital parameters for the "gold sample" binaries (Table 3 in PW20)
  <https://users.flatironinstitute.org/~apricewhelan/data/dr16-binaries/gold_sample.fits>`_ (1,023 sources)

  This file contains maximum *a posteriori* values of the orbital parameters for
  binary systems that have unimodal (i.e., uniquely determined) posterior
  samplings; additional quality cuts are described in PW20. The uncertainties on
  the orbital parameters (`_err` columns) are estimated using percentiles from
  the 1D (marginal) distributions.  Along with the orbital parameter columns,
  this file also contains all columns from the APOGEE DR16 allStar file, the
  Gaia DR2 source file, and primary star mass estimates from the STARHORSE2019
  catalog of stellar parameters.

* `Orbital parameters for binaries with bimodal samplings
  <https://users.flatironinstitute.org/~apricewhelan/data/dr16-binaries/bimodal.fits>`_ (551 sources)

  This table contains two rows per system for all systems with bimodal posterior
  samplings over orbital period. Within each mode, the maximum *a posteriori*
  sample is reported.

* `Metadata for all APOGEE sources in the parent sample (Table 2 in PW20)
  <https://users.flatironinstitute.org/~apricewhelan/data/dr16-binaries/metadata.fits>`_ (232,495 sources)

  This file contains metadata computed from the orbital parameter samplings for
  all APOGEE stars in our parent sample. See the description of Table 2 in PW20.

* `Metadata for APOGEE sources identified as candidate binary star systems <https://users.flatironinstitute.org/~apricewhelan/data/dr16-binaries/lnK0.0_logL4.6_metadata.fits>`_ (19,635 sources)

  This file contains the same columns as in Table 2 and in the metadata file
  above, but only contains sources that were identified as candidate binary star
  systems based on the orbital parameter samplings.


Tutorials
=========

Coming soon!
