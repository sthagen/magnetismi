import pathlib

from magnetismi import ENCODING

CS = ('n', 'm', 'gnm', 'hnm', 'dgnm', 'dhnm')
STORE_PATH = pathlib.Path('magnetismi', 'model')
TWIN_END_TOKEN = '9' * 48


class Coefficients:
    """The WMM coefficients relevant to the year given."""

    years_covered = tuple(y for y in range(2020, 2025 + 1))
    model_from_year = {y: '2020' for y in range(2020, 2025 + 1)}
    model = {}

    def load(self, model_year: int) -> None:
        """Load the model."""
        with open(STORE_PATH / f'wmm-{model_year}.txt', 'rt', encoding=ENCODING) as handle:
            recs = [line.strip().split() for line in handle if line.strip() and line.strip() != TWIN_END_TOKEN]

        epoc, model, model_date_string = recs[0]
        self.model['epoch'] = float(epoc)
        self.model['model_code'] = model
        self.model['model_date_string'] = model_date_string

        self.model['coeffs'] = [
            {c: int(r[s]) if c in ('n', 'm') else float(r[s]) for s, c in enumerate(CS)}
            for r in recs[1:]
            if len(r) == len(CS)
        ]

    def __init__(self, year: int):
        """Initialize the mode from file in case it covers the requested year."""
        if year not in self.years_covered:
            raise ValueError(f'requested year ({year}) not within {self.years_covered}')

        self.model = {
            'year_requested': year,
            'model_id': self.model_from_year[year],
        }
        self.load(self.model['model_id'])
