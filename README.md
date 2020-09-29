# aloxide-sdk-python

Aloxide SDK for Python is a collection of libraries which allow you to access various blockchains.

## Development

Setup virtual environment:

```bash
$ python3 -m venv aloxide-sdk
$ source aloxide-sdk/bin/activate
$ pip install wheel
$ pip install setuptools
$ pip install twine
```

```bash
# test
$ python setup.py pytest

# build
$ python setup.py bdist_wheel

# install
$ pip install dist/aloxidesdk-0.1.0-py3-none-any.whl
```

Once you have installed `aloxidesdk` library, you can import it using:

```python
import aloxidesdk
from aloxidesdk import utils

# more code go here
```
