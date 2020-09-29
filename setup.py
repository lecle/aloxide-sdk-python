from setuptools import find_packages, setup

with open('requirements.txt') as requirements:
  requires = list(requirements)

setup(
  name = 'aloxidesdk',
  version = '0.1.0',
  description = 'Aloxide SDK for Python is a collection of libraries which allow you to access various blockchains',
  author = 'Lecle',
  url = 'https://github.com/lecle/aloxide-sdk-python',
  license = 'Apache-2.0',
  packages = find_packages(include = ['aloxidesdk']),
  install_requires = requires,
  setup_requires = ['pytest-runner==4.4'],
  test_suite = 'tests',
  tests_require = ['pytest==4.4.1']
)
