def top_level_packages(setup):
    """Extract the top-level packages defined in a setup file."""
    packages = sorted(set(setup['packages']) - set(setup.get('namespace_packages', [])))
    i = 0
    while i < len(packages):
        q = packages[i] + '.'
        i += 1
        packages = packages[:i] + [p for p in packages[i:] if not p.startswith(q)]
    return sorted(packages)


def read_setup(project_dir):
    """Read the setup metadata from a directory.

    Warning: This function imports the setup file while mocking
    ``setuptools.setup``; any other code in ``setup.py`` gets
    executed.

    """
    import os
    import setuptools
    from _pytest.monkeypatch import monkeypatch

    setup = {}
    mp = monkeypatch()
    try:
        mp.chdir(project_dir)
        mp.setattr(setuptools, 'setup', setup.update)

        with open('setup.py') as f:
            exec(
                compile(
                    f.read(),
                    os.path.abspath(f.name),
                    "exec"),
                {'__file__': f.name})
    finally:
        mp.undo()
    return setup
