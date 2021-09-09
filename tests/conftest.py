from pathlib import Path

import pytest


@pytest.fixture
def basedir(request: pytest.FixtureRequest, datadir) -> Path:
    if request.cls is not None:
        return datadir / request.cls.__name__ / request.function.__name__

    return datadir / request.function.__name__
