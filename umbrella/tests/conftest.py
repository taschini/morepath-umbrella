import pytest
from ..helpers import get_subproject_dirs


@pytest.fixture(params=get_subproject_dirs())
def subproject(request, monkeypatch):
    """Iterate over the subprojects.

    Temporarily changes the current directory to the subproject.

    """
    monkeypatch.chdir(request.param)
