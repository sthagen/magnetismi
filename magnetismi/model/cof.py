import pathlib

from magnetismi import ENCODING

CS = ('n', 'm', 'gnm', 'hnm', 'dgnm', 'dhnm')
STORE_PATH = pathlib.Path('magnetismi', 'model')
TWIN_END_TOKEN = '9' * 48


class Coefficients:
    """The WMM coefficients relevant to the year given."""

    years_covered = tuple(y for y in range(2020, 2025 + 1))
    model_from_year = {y: '2020' for y in range(2020, 2025 + 1)}
    data = []

    def __init__(self, year: int):
        """Verify we cover the year requested and if covered load the coefficients."""
        if year not in self.years_covered:
            raise ValueError(f'requested year ({year}) not within {self.years_covered}')

        self.year = year
        self.model_year = self.model_from_year[self.year]
        with open(STORE_PATH / f'wmm-{self.model_year}.txt', 'rt', encoding=ENCODING) as handle:
            recs = [line.strip().split() for line in handle if line.strip() and line.strip() != TWIN_END_TOKEN]

        epoc, model, modeldate = recs[0]
        self.epoch = float(epoc)
        self.model = model
        self.modeldate = modeldate

        self.data = [
            {c: int(r[s]) if c in ('n', 'm') else float(r[s]) for s, c in enumerate(CS)}
            for r in recs[1:]
            if len(r) == len(CS)
        ]
