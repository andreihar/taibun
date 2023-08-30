from setuptools import setup, find_packages

VERSION = '0.0.9'

# Setting up
setup(
    name='taibun',
    version=VERSION,
    packages=find_packages(),
    package_dir={'taibun': 'taibun'},
    package_data={'taibun': ['data/*.json']},
)