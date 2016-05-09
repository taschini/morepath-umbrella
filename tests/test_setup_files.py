import pytest


@pytest.yield_fixture(scope="module")
def collect():
    """Return a list that is used as an accumulator.

    At the end the list is saved in a pickle file called 'setups.pkl'.

    """
    collection = []
    try:
        yield collection
    finally:
        try:
            import cPickle as pickle
        except ImportError:
            import pickle
        with open('setups.pkl', 'wb') as f:
            pickle.dump(collection, f, -1)


def test_setup_file(subproject, monkeypatch, collect):
    import os
    import six
    import setuptools

    setup = {}

    monkeypatch.setattr(setuptools, 'setup', setup.update)

    # The setup file can be actually interpreted by Python
    namespace = {'__file__': 'setup.py'}
    exec(compile(
        open('setup.py').read(),
        os.path.abspath('setup.py'),
        "exec"), namespace)

    collect.append(setup)

    # The long_description field is unicode
    assert isinstance(setup['long_description'], six.text_type)

    # The license is BSD
    assert setup['license'] == 'BSD'

    # The library name is the same as the project name
    assert os.path.basename(os.getcwd()) == setup['name']


def test_flake8_setup(subproject):
    from flake8.main import check_file

    assert check_file('setup.py') == 0
