# Usage

## Help

```console
❯ magnetismi
usage: magnetismi [-h] --latitude LAT_DD --longitude LON_DD [--altitude ALT_FT]
                  [--date DATE] [--quiet] [--verbose] [date_pos]

Magnetism (Finnish: magnetismi) - another opinionated World Magnetic Model calculator.

positional arguments:
  date_pos            date for magentic calculation in YYYY-mm-dd or fractional year decimal format. Optional
                      (default: empty for current date)

options:
  -h, --help          show this help message and exit
  --latitude LAT_DD   geodetic latitude in decimal degrees inside [-180, +180]
  --longitude LON_DD  geodetic longitude in decimal degrees inside [-90, +90]
  --altitude ALT_FT   altitude in feet inside [-3280.84, +2788714]. Optional (default: 0)
  --date DATE         date for magentic calculation in YYYY-mm-dd or fractional year decimal format. Optional
                      (default: positional date value)
  --quiet, -q         work as quiet as possible - progress bar only if all well (default: False)
  --verbose, -v       work logging more information along the way (default: False)
```

## Example from Reference Tests

```console
❯ magnetismi 2020.0 --latitude 89 --longitude -112 --altitude 91863.518
2022-10-09T14:48:49.186216+00:00 INFO [MAGNETISMI]: starting calculation at 2020-01-01 for alt_ft=91863.518, lat_dd=89.0, and lon_dd=-112.0
2022-10-09T14:48:49.193795+00:00 INFO [MAGNETISMI]: - fetched model with id 2020
2022-10-09T14:48:49.194273+00:00 INFO [MAGNETISMI]: - result for data.time=2020.0, data.alt=91863.518, data.lat=89.0, and data.lon=-112.0:
2022-10-09T14:48:49.194327+00:00 INFO [MAGNETISMI]:   Declination D = -103.5163531623186, inclination I = 88.38304329670308 in degrees
2022-10-09T14:48:49.194363+00:00 INFO [MAGNETISMI]:   North X = -369.8281156939691, East Y = -1538.510359219206, Down Z = 56054.129233369335 component in nT
2022-10-09T14:48:49.194395+00:00 INFO [MAGNETISMI]:   Horizontal H = 1582.3359190078959, total T = 56076.45843909771 intensity in nT
2022-10-09T14:48:49.194428+00:00 INFO [MAGNETISMI]: calculation complete after 0.008616 seconds
INP(time=2020.0, alt=91863.518, lat=89.0, long=-112.0)
OUT(D=-103.5163531623186, I=88.38304329670308, X=-369.8281156939691, Y=-1538.510359219206, Z=56054.129233369335, H=1582.3359190078959, T=56076.45843909771)
```

Or, in quiet mode:

```console
❯ magnetismi 2020.0 --latitude 89 --longitude -112 --altitude 91863.518 -q
INP(time=2020.0, alt=91863.518, lat=89.0, long=-112.0)
OUT(D=-103.5163531623186, I=88.38304329670308, X=-369.8281156939691, Y=-1538.510359219206, Z=56054.129233369335, H=1582.3359190078959, T=56076.45843909771)
```

When all works well, quiet mode is essentially like redirecting stderr to `/dev/null`:

```console
❯ magnetismi 2020.0 --latitude 89 --longitude -112 --altitude 91863.518 2> /dev/null
INP(time=2020.0, alt=91863.518, lat=89.0, long=-112.0)
OUT(D=-103.5163531623186, I=88.38304329670308, X=-369.8281156939691, Y=-1538.510359219206, Z=56054.129233369335, H=1582.3359190078959, T=56076.45843909771)
```

### Error Cases

Missing latitude and longitude:

```console
❯ magnetismi 2020-01-01
usage: magnetismi [-h] --latitude LAT_DD --longitude LON_DD [--altitude ALT_FT] [--date DATE] [--quiet] [--verbose] [date_pos]
magnetismi: error: the following arguments are required: --latitude, --longitude
```

Latitude outside of valid range:

```console
❯ magnetismi 2020-01-01 --latitude 91 --longitude -112
usage: magnetismi [-h] --latitude LAT_DD --longitude LON_DD [--altitude ALT_FT] [--date DATE] [--quiet] [--verbose] [date_pos]
magnetismi: error: requested latitude (91.0) is outside of [-90, +90] degrees
```

Date requested not in scope of model:

```console
❯ magnetismi 202.0 --latitude 89 --longitude -112
usage: magnetismi [-h] --latitude LAT_DD --longitude LON_DD [--altitude ALT_FT] [--date DATE] [--quiet] [--verbose] [date_pos]
magnetismi: error: requested year (202) is outside of (2020, 2021, 2022, 2023, 2024, 2025)
```

Altitude above valid upper value:

```console
❯ magnetismi 2020-01-01 --altitude 3000000 --latitude 89 --longitude -112
usage: magnetismi [-h] --latitude LAT_DD --longitude LON_DD [--altitude ALT_FT] [--date DATE] [--quiet] [--verbose] [date_pos]
magnetismi: error: requested altitude (3000000.0) is outside of [-3280.84, +2788714] feet and the model is only valid between the corresponding [-1, +850] km
```
