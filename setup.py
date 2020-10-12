from setuptools import find_packages, setup

with open('requirements.txt') as requirements:
  requires = list(requirements)

with open('README.md', 'r') as readme:
  long_description = readme.read()

setup(
  name = 'aloxidesdk',
  version = '0.1.3',
  description = 'Aloxide SDK for Python is a collection of libraries which allow you to access various blockchains',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  keywords = ['blockchain', 'icon', 'eosio'],
  author = 'Lecle',
  url = 'https://github.com/lecle/aloxide-sdk-python',
  license = 'Apache-2.0',
  packages = find_packages(include = ['aloxidesdk']),
  python_requires = '>=3.7',
  install_requires = requires,
  setup_requires = ['pytest-runner==4.4'],
  test_suite = 'tests',
  tests_require = ['pytest==4.4.1']
)
