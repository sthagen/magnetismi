# API

## Programmatic Usage Help

``` python
import magnetismi.magnetismi as api

help(api)
```

## Example Programmatic Calculation of Declination

Using the first reference test from upstream model providers and calculating
the declination at that date (start of 2020) and two years later:

```python
>>> import magnetismi.magnetismi as api
>>> from magnetismi import FEET_TO_KILOMETER
>>> model = api.Model(2022)  # Any year within valid range of model will do
>>> alt_ft = 28 / FEET_TO_KILOMETER  # Reference point is given in kilometers 
>>> model.at(lat_dd=89, lon_dd=-121, alt_ft=alt_ft, date=api.dti.date(2020, 1, 1)).dec
-112.40998916672564
>>> model.at(lat_dd=89, lon_dd=-121, alt_ft=alt_ft, date=api.dti.date(2022, 1, 1)).dec
-107.15773983508477
```
