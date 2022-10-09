"""Command line interface for splice (Finnish liitos) contributions."""
import argparse
import datetime as dti
import pathlib
import sys
from typing import List, Union

import magnetismi.magnetismi as api
from magnetismi import APP_ALIAS, APP_NAME, date_from_fractional_year

DATE_FORMAT = '%Y-%m-%d'


def parse_request(argv: List[str]) -> Union[int, argparse.Namespace]:
    """DRY."""
    parser = argparse.ArgumentParser(
        prog=APP_ALIAS, description=APP_NAME, formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--latitude',
        dest='lat_dd',
        type=float,
        required=True,
        help='geodetic latitude in decimal degrees inside [-180, +180]',
    )
    parser.add_argument(
        '--longitude',
        dest='lon_dd',
        type=float,
        required=True,
        help='geodetic longitude in decimal degrees inside [-90, +90]',
    )
    parser.add_argument(
        '--altitude',
        dest='alt_ft',
        type=float,
        default=0,
        help='altitude in feet. Optional\n(default: 0)',
    )
    parser.add_argument(
        '--date',
        dest='date',
        default='',
        help='date for magentic calculation in YYYY-mm-dd format. Optional\n(default: positional date value)',
        required=False,
    )
    parser.add_argument(
        'date_pos',
        nargs='?',
        default='',
        help='date for magentic calculation in YYYY-mm-dd format. Optional\n(default: empty for current date)',
    )
    parser.add_argument(
        '--quiet',
        '-q',
        dest='quiet',
        default=False,
        action='store_true',
        help='work as quiet as possible - progress bar only if all well (default: False)',
    )
    parser.add_argument(
        '--verbose',
        '-v',
        dest='verbose',
        default=False,
        action='store_true',
        help='work logging more information along the way (default: False)',
    )
    if not argv:
        parser.print_help()
        return 0

    options = parser.parse_args(argv)

    if options.verbose and options.quiet:
        parser.error('you cannot be quiet and verbose at the same time')

    if options.date:
        try:
            options.date_in = dti.datetime.strptime(options.date, DATE_FORMAT).date()
        except ValueError as err:
            parser.error(f'requested date ({options.date}) does not parse as YYYY-mm-dd; error: {err}')
    else:
        if options.date_pos:
            try:
                options.date_in = dti.datetime.strptime(options.date_pos, DATE_FORMAT).date()
            except ValueError as err:
                parser.error(
                    f'requested (positional) date ({options.date_pos}) does not parse as YYYY-mm-dd; error: {err}'
                )
        else:
            options.date_in = dti.date.today()

    if not -90 <= options.lat_dd <= 90:
        parser.error(f'requested latitude ({options.lat_dd}) is outside of [-90, +90] degrees')

    if not -180 <= options.lon_dd <= 180:
        parser.error(f'requested longitude ({options.lon_dd}) is outside of [-180, +180] degrees')

    return options


def main(argv: Union[List[str], None] = None) -> int:
    """Delegate processing to functional module."""
    argv = sys.argv[1:] if argv is None else argv
    options = parse_request(argv)
    if isinstance(options, int):
        return 0
    return api.calc(options)
