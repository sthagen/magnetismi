import datetime as dti

import magnetismi.magnetismi as api


def test_magnetism_tc_1():
    model = api.Model(2022)
    data = model.at(lat_dd=89, lon_dd=-121, alt_ft=91863.518, date=dti.date(2020, 1, 1))

    assert data.dec == -112.40998917104227
    assert data.dip == 88.45768418685287
    assert data.bx == -575.6658556786076
    assert data.by == -1395.979205963626
    assert data.bz == 56082.32776941662
    assert data.bh == 1510.0162651034655
    assert data.lat == 89
    assert data.lon == -121
    assert data.alt == 91863.518
    assert data.ti == 56102.65267487051
