# magnetismi

Magnetism (Finnish: magnetismi) - another opinionated World Magnetic Model calculator.

[License: MIT](https://git.sr.ht/~sthagen/magnetismi/tree/default/item/LICENSE)

[![version](https://img.shields.io/pypi/v/magnetismi.svg?style=flat)](https://pypi.python.org/pypi/magnetismi/)
[![downloads](https://pepy.tech/badge/magnetismi/month)](https://pepy.tech/project/magnetismi)
[![wheel](https://img.shields.io/pypi/wheel/magnetismi.svg?style=flat)](https://pypi.python.org/pypi/magnetismi/)
[![supported-versions](https://img.shields.io/pypi/pyversions/magnetismi.svg?style=flat)](https://pypi.python.org/pypi/magnetismi/)
[![supported-implementations](https://img.shields.io/pypi/implementation/magnetismi.svg?style=flat)](https://pypi.python.org/pypi/magnetismi/)

## Model

### Interface to the Source Data

The mode in use is the current World Magnetic Model from 2020 \[[WMM20](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2020/WMM2020_Report.pdf)\] with is considered valid through 2025. 
For information on the state of the geomagnetic field the latest report is per [December 2021](https://www.ngdc.noaa.gov/geomag/WMM/data/WMMReports/WMM_Annual_Report_2021.pdf)
The corresponding coefficient file is per [WMM2020COF.zip](https://www.ngdc.noaa.gov/geomag/WMM/soft.shtml#).
The COF file format is documented on the page [WMM coefficient file format for developers](https://www.ngdc.noaa.gov/geomag/WMM/wmmformat.shtml) including example code to read the coefficients. 

### The Magnetic Elements

Citing the model report \[WMM20] section 1.1.1:
>The geomagnetic field vector, Bm, is described by seven elements. These are the northerly intensity X, the easterly intensity Y, the vertical intensity Z (positive downwards) and the following quantities derived from X, Y and Z: the horizontal intensity H, the total intensity F, the inclination angle I, (also called the dip angle and measured from the horizontal plane to the field vector, positive downwards) and the declination angle D (also called the magnetic variation and measured clockwise from true north to the horizontal component of the field vector). In the descriptions of X, Y, Z, H, F, I and D above, the vertical direction is perpendicular to the WGS 84 ellipsoid model of the Earth, the horizontal plane is perpendicular to the vertical direction, and the rotational directions clockwise and counter-clockwise are determined by a view from above \[...]
>
>The quantities X, Y and Z are the sizes of perpendicular vectors that add vectorially to Bm. Conversely, X, Y and Z can be determined from the quantities F, I and D (i.e., the quantities that specify the size and direction of Bm).

#### Ranges of the Magnetic Element Values

The below table depicts the expected value ranges of the magnetic field elements (Source: \[[WMM20](https://www.ngdc.noaa.gov/geomag/WMM/data/WMM2020/WMM2020_Report.pdf)\] table 1 in section 1.1.1):

| Element | Name                 | Alternative Name    | Range and unit at Earth’s Surface | Directional Hint |
|:-------:|:-------------------- |:------------------- |:--------------------------------- |:---------------- |
|    X    | North component      | Northerly intensity | \[-17000, 43000\] nT              | North            |
|    Y    | East component       | Easterly intensity  | \[-18000, 17000\] nT              | East             |
|    Z    | Down component       | Vertical intensity  | \[-67000, 62000\] nT              | Down             |
|    H    | Horizontal intensity |                     | \[0, 43000\] nT                   |                  |
|    F    | Total intensity      | Total field         | \[23000, 67000\] nT               |                  |
|    I    | Inclination          | Dip                 | \[-90, 90\] Degree                | Down             |
|    D    | Declination          | Magnetic variation  | \[-180, 180\] Degree              | East / Clockwise |
|    GV   | Grid Variation       | Grivation           | \[-180, 180\] Degree              | East / Clockwise |

## Documentation

User and developer [documentation of magnetismi](https://codes.dilettant.life/docs/magnetismi).

## Bug Tracker

Feature requests and bug reports are best entered in the [todos of magnetismi](https://todo.sr.ht/~sthagen/magnetismi).

## Primary Source repository

The primary source of `magnetismi` lives somewhere on a mountain in Central Switzerland.
But, we use decentralized version control (git), so any clone can become the source to everyone's benefit, no central only code.
Anyway, the preferred public clones of `magnetismi` are:

* [on codeberg](https://codeberg.org/sthagen/magnetismi) - a democratic community-driven, non-profit software development platform operated by Codeberg e.V.
* [at sourcehut](https://git.sr.ht/~sthagen/magnetismi) - a collection of tools useful for software development.

## Status

Experimental

**Note**: The default branch is `default`.
