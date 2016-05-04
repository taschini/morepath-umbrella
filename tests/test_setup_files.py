def test_setup_file(subproject, monkeypatch):
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

    # THe long_description field is unicode
    assert isinstance(setup['long_description'], six.text_type)
