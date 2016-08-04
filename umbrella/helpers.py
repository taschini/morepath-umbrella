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


def get_subproject_dirs():
    """List the sub-project directories."""
    import os.path as op
    import glob
    pattern = op.join(op.dirname(__file__), '..', 'src', '*')
    return [d for d in glob.glob(pattern) if op.isdir(d)]


def source_packages():
    """List the source packages in the sub-projects."""
    import os

    dirs = []
    for d in get_subproject_dirs():
        d = os.path.relpath(d)
        pkgs = top_level_packages(read_setup(d))
        dirs.extend(os.path.join(d, p.replace('.', os.sep)) for p in pkgs)

    return dirs


def browser_url(scm):
    """Return a browser friendly URL for SCM specification.

    This function works only with a limited subset of SCM specifications.

    """
    kind, url = scm.split()
    if kind == 'git':
        if url.startswith('git@github.com:'):
            url = url.replace('git@github.com:', 'https://github.com/')
        if url.endswith('.git'):
            url = url[:-4]
        return url
    return ''


def get_sources():
    "Get the checked-out libraries as pairs (name, url) organized by section."
    from six.moves.configparser import SafeConfigParser

    parser = SafeConfigParser()
    assert parser.read('buildout.cfg') == ['buildout.cfg']
    # with io.open('buildout.cfg', encoding='utf-8') as f:
    #     parser.readfp(f)

    from collections import OrderedDict
    result = OrderedDict()

    for k in 'libraries', 'extensions', 'examples':
        result[k] = [(name, browser_url(scm)) for name, scm in parser.items('sources.' + k)]

    return result


def get_jinja_env():
    "Return the set of templates used for rendering."
    import jinja2
    return jinja2.Environment(loader=jinja2.PackageLoader(__package__))


def write_text(path, text):
    "Write unicode text to path."
    import io
    with io.open(path, 'wt', encoding='utf-8') as f:
        f.write(text)


def list_autoscan_fixtures():
    """List the packages used as test fixtures for autoscan."""
    import os
    from glob import glob
    root = os.path.join(os.path.dirname(__file__), '..')
    pattern = os.path.join(root, 'src', 'morepath', 'fixture_packages', '*')
    return [os.path.relpath(d, root) for d in glob(pattern)]
