from pathlib import Path

import pytest

from mp.main import handle


def test_handle_01():
    # -- setup
    not_found_path = Path("foobar")

    # -- exercise
    # -- verify
    with pytest.raises(FileNotFoundError):
        handle(filepath=not_found_path)


def test_handle_02(basedir: Path):
    # -- setup
    filepath = basedir / "test.md"

    # -- exercise
    handle(filepath=filepath)

    # -- verify
    tmpfile = basedir / "test.mp"
    assert not tmpfile.exists()
