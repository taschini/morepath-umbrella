.PHONY: all clean status

targets := README.md requirements.txt setup.cfg ackdirs.txt

all: $(targets)

README.md: buildout.cfg umbrella/templates/README.md
	python -m umbrella readme --output $@

requirements.txt: buildout.cfg umbrella/templates/requirements.txt
	python -m umbrella deps --output $@

setup.cfg: buildout.cfg umbrella/templates/setup.cfg
	python -m umbrella setupcfg --output $@

ackdirs.txt: buildout.cfg
	python -m umbrella pkgdirs --output $@

clean:
	-rm $(targets)

status:
	@ for k in src/*; do (cd $$k; printf '%-30s ' $$k; git status -sb); done

# This has been used for bootstrapping only.
src/morepath/doc/examples.rst: buildout.cfg umbrella/templates/examples.rst
	python -m umbrella examples --output $@
