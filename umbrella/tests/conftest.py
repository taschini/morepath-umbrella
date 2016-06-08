import pytest


def get_subproject_dirs():
    import os.path as op
    import glob
    pattern = op.join(op.dirname(__file__), '..', 'src', '*')
    return [d for d in glob.glob(pattern) if op.isdir(d)]


@pytest.fixture(params=get_subproject_dirs())
def subproject(request, monkeypatch):
    """Iterate over the subprojects.

    Temporarily changes the current directory to the subproject.

    """
    monkeypatch.chdir(request.param)
