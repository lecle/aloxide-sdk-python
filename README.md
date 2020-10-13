# Aloxide SDK for Python

Aloxide SDK for Python is a collection of libraries which allow you to access various blockchains.

## Requirements

Aloxide SDK for Python development and execution requires Python 3.7 or later.

## Dependencies

[ICON SDK for Python](https://github.com/icon-project/icon-sdk-python)

[EosPy](https://github.com/lecle/eospy)

## Development

[Gitpod](https://www.gitpod.io/) is an online open source VS Code-like IDE (and is free for open source projects) for working on issues and making PRs to this project. With a single click it will start a workspace automatically.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/lecle/aloxide-sdk-python)

Setup a virtual environment, do it once:

```bash
$ cd aloxide-sdk-python
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install wheel
$ pip install setuptools
$ pip install twine
```

And following are commands you will use during development:

```bash
# test
$ python setup.py pytest

# build
$ rm -rf dist && python setup.py sdist bdist_wheel

# install from source for testing in other projects
$ pip install -e /path/to/aloxide-sdk-python
```

## Publish to PyPI

It’s time to upload your package to the PyPI so others can use it. The first thing you’ll need to do is register an account on [TestPyPI](https://test.pypi.org/).

```bash
$ twine upload --repository testpypi dist/*
```

Once uploaded the package should be viewable on TestPyPI at [https://test.pypi.org/project/aloxidesdk](https://test.pypi.org/project/aloxidesdk).

## Usage

First, you need to get Aloxide SDK for Python into your project. It can be installed using pip as follows:

```bash
$ pip install aloxidesdk
```

Once you have installed `aloxidesdk` library, you can import it using:

```python
import aloxidesdk
from aloxidesdk.aloxide_service import AloxideService

# more code go here
```

More examples are found on GitHub at [examples](https://github.com/lecle/aloxide-sdk-python/tree/master/examples).
