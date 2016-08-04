import opster
import sys
from .helpers import (
    get_jinja_env,
    get_sources,
    get_subproject_dirs,
    list_autoscan_fixtures,
    read_setup,
    source_packages,
    write_text,
)


@opster.command()
def readme(output=('o', '/dev/stdout', 'the output "readme" file')):
    """Generate readme file from buildout configuration."""
    template = get_jinja_env().get_template('README.md')
    write_text(output, template.render(**get_sources()))


@opster.command()
def deps(output=('o', '/dev/stdout', 'the output requirements file')):
    """Generate requirements file for use with pip."""
    template = get_jinja_env().get_template('requirements.txt')
    write_text(output, template.render(fixtures=list_autoscan_fixtures(), **get_sources()))


@opster.command()
def setupcfg(output=('o', '/dev/stdout', 'the output setup.cfg file')):
    """Generate a setup configuration file."""
    template = get_jinja_env().get_template('setup.cfg')
    write_text(output, template.render(dirs=source_packages()))


@opster.command()
def pkgdirs(output=('o', '/dev/stdout', 'the output requirements file')):
    """Generate list of package directories."""
    write_text(output, u'\n'.join(source_packages()) + '\n')


@opster.command()
def examples(output=('o', '/dev/stdout', 'the output requirements file')):
    """Generate the examples page for Morepath docs."""
    template = get_jinja_env().get_template('examples.rst')
    setups = {s['name']: s for s in (read_setup(d) for d in get_subproject_dirs())}
    examples = [(label, link, 'https://pypi.python.org/pypi/' + label, setups[label]['description'])
                for label, link in get_sources()['examples']]
    write_text(output, template.render(examples=examples))


if __name__ == '__main__':
    sys.exit(opster.dispatch(scriptname='python -m ' + __package__))
