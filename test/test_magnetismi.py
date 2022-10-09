import datetime as dti

import pytest

import magnetismi.magnetismi as api
from magnetismi import FEET_TO_KILOMETER


def test_magnetism_tc_1():
    model = api.Model(2022)
    doi = ('date', 'alt_km', 'lat_dd', 'lon_dd', 'dec', 'dip', 'bh', 'bx', 'by', 'bz', 'ti')
    vector = (
        2020.0,
        28,
        89,
        -121,
        -112.41,
        88.46,
        1510.0,
        -575.7,
        -1396.0,
        56082.3,
        56102.7,
        2.6,
        0.0,
        -18.0,
        69.5,
        -9.2,
        20.1,
        19.6,
    )
    voi = {d: v for d, v in zip(doi, vector)}
    voi['alt_ft'] = voi['alt_km'] / FEET_TO_KILOMETER

    data = model.at(lat_dd=voi['lat_dd'], lon_dd=voi['lon_dd'], alt_ft=voi['alt_ft'], date=dti.date(2020, 1, 1))

    assert data.time == pytest.approx(voi['date'], 0.01)
    assert data.alt == pytest.approx(voi['alt_ft'], 0.01)  # 91863.518
    assert data.lat == pytest.approx(voi['lat_dd'], 0.01)  # 89
    assert data.lon == pytest.approx(voi['lon_dd'], 0.01)  # -121
    assert data.dec == pytest.approx(voi['dec'], 0.01)  # -112.40998917104227
    assert data.dip == pytest.approx(voi['dip'], 0.01)  # 88.45768418685287
    assert data.bh == pytest.approx(voi['bh'], 0.01)  # 1510.0162651034655
    assert data.bx == pytest.approx(voi['bx'], 0.01)  # -575.6658556786076
    assert data.by == pytest.approx(voi['by'], 0.01)  # -1395.979205963626
    assert data.bz == pytest.approx(voi['bz'], 0.01)  # 56082.32776941662
    assert data.ti == pytest.approx(voi['ti'], 0.01)  # 56102.65267487051
