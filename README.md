Morepath Umbrella
=================

This project puts together the Morepath framework with related projects:

* The libraries developed together with Morepath:
  - [bowerstatic](https://github.com/faassen/bowerstatic)
  - [dectate](https://github.com/morepath/dectate)
  - [importscan](https://github.com/faassen/importscan)
  - [morepath](https://github.com/morepath/morepath)
  - [reg](https://github.com/morepath/reg)
* The extensions developed and supported within the [Morepath organization on GitHub](https://github.com/morepath):
  - [more.basicauth](https://github.com/morepath/more.basicauth)
  - [more.chameleon](https://github.com/morepath/more.chameleon)
  - [more.forwarded](https://github.com/morepath/more.forwarded)
  - [more.itsdangerous](https://github.com/morepath/more.itsdangerous)
  - [more.jinja2](https://github.com/morepath/more.jinja2)
  - [more.jwtauth](https://github.com/morepath/more.jwtauth)
  - [more.mako](https://github.com/morepath/more.mako)
  - [more.static](https://github.com/morepath/more.static)
  - [more.transaction](https://github.com/morepath/more.transaction)
  - [more.webassets](https://github.com/morepath/more.webassets)
* The example applications developed and supported within the [Morepath organization on GitHub](https://github.com/morepath):
  - [morepath_batching](https://github.com/morepath/morepath_batching)
  - [morepath_cerebral_todomvc](https://github.com/morepath/morepath_cerebral_todomvc)
  - [morepath_reactredux](https://github.com/morepath/morepath_reactredux)
  - [morepath_rest_dump_load](https://github.com/morepath/morepath_rest_dump_load)
  - [morepath_sqlalchemy](https://github.com/morepath/morepath_sqlalchemy)
  - [morepath_static](https://github.com/morepath/morepath_static)
  - [morepath_wiki](https://github.com/morepath/morepath_wiki)

Quickstart
==========

Installation
------------

1. Clone recursively this repository:

   ```shell
   git clone --recursive git@github.com:taschini/morepath-umbrella.git
   cd morepath-umbrella
   ```

2. Use Buildout to check out all the project listed above:

   ```shell
   mkdir env
   virtualenv --no-site-packages env/buildout
   ./env/buildout/bin/python bootstrap.py
   ./bin/buildout
   ```

3. Create as many virtual environments as the versions of Python you
   want to use for testing, at least two, one for Python 2.7 and one
   for Python 3.5:

   ```shell
   virtualenv --no-site-packages -p python2.7 env/py27
   virtualenv --no-site-packages -p python3.5 env/py35
   ```

4. Use Pip to install all the dependencies:

   ```shell
   for k in ./env/py*; do $k/bin/pip install -r requirements.txt ; done
   ```

Note on the installation on OS X
--------------------------------

On some versions of OS X, you might have to ensure that the
[Cryptography](https://cryptography.io/en/latest/installation/#building-cryptography-on-os-x)
library for Python is linked to a recent version of OpenSSL:

```shell
brew install openssl
export CRYPTOGRAPHY_OSX_NO_LINK_FLAGS=1
export LDFLAGS="$(brew --prefix openssl)/lib/libssl.a $(brew --prefix openssl)/lib/libcrypto.a"
export CFLAGS="-I$(brew --prefix openssl)/include"
for k in ./env/py*; do $k/bin/pip install cryptography --no-binary :all:
```

Common tasks
------------

*  Running the tests using one of the virtual environments (say that for Python 3.5):

   ```shell
   ./env/py35/bin/py.test
   ```

*  Running the tests with coverage statistics:

   ```shell
   ./env/py35/bin/py.test --cov
   ```

*  Searching *text* in the projects under the umbrella using
   [Ack](http://beyondgrep.com/install/):

   ```shell
   ack text `cat ackdirs.txt`
   ```

*  Check status and branch names of all the projects under the umbrella:

   ```shell
   make status
   ```
