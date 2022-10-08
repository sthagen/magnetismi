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

    def __init__(self, year: int):
        """Verify we cover the year requested and if covered load the coefficients."""
        if year not in self.years_covered:
            raise ValueError(f'requested year ({year}) not within {self.years_covered}')

        self.model = {
            'year_requested': year,
            'model_year': self.model_from_year[year],
        }
        with open(STORE_PATH / f'wmm-{self.model["model_year"]}.txt', 'rt', encoding=ENCODING) as handle:
            recs = [line.strip().split() for line in handle if line.strip() and line.strip() != TWIN_END_TOKEN]

        epoc, model, modeldate = recs[0]
        self.model['epoch'] = float(epoc)
        self.model['model_code'] = model
        self.model['model_date_string'] = modeldate

        self.model['coeffs'] = [
            {c: int(r[s]) if c in ('n', 'm') else float(r[s]) for s, c in enumerate(CS)}
            for r in recs[1:]
            if len(r) == len(CS)
        ]
