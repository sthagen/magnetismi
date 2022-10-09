import calendar
import datetime as dti

ABS_LAT_DD_ANY_ARCITC = 55.0
DEFAULT_MAG_VAR = -999.0
ENCODING = 'utf-8'
FEET_TO_KILOMETER = 1.0 / 3280.8399


def date_from_fractional_year(date: float) -> dti.date:
    """Going back ..."""
    y_int = int(date)
    rest_y_float = date - y_int
    days_in_year = 365 + calendar.isleap(y_int)
    rest_d_float = round(rest_y_float * days_in_year, 1)
    if rest_d_float:
        day_counts = [c for _, c in (calendar.monthrange(y_int, m) for m in range(1, 12 + 1))]
        day_cum = [day_counts[0]] + [0] * 11
        for m, c in enumerate(day_counts[1:], start=2):
            day_cum[m - 1] = day_cum[m - 2] + c
        m_int = 1  # Well, not really, but, ... happy linter
        for m, c in enumerate(day_cum, start=1):
            if c < rest_d_float:
                continue
            m_int = m
            break

        d_int = int(rest_d_float - day_cum[m_int - 2])
    else:
        m_int, d_int = 1, 1
    return dti.date(y_int, m_int, d_int)


def fractional_year_from_date(date: dti.date) -> float:
    """... and forth."""
    days_in_year = float(365 + calendar.isleap(date.year))
    return date.year + ((date - dti.date(date.year, 1, 1)).days / days_in_year)
