from setuptools import setup, find_packages

setup(
    name='rontgen',
    version='0.1',
    author='Steven Christe',
    author_email='',
    url='',
    license='See LICENSE.txt',
    packages=find_packages(),
    package_data={'': ['data/*.json', 'data/elements/*.csv', 'data/compounds_mixtures/*.csv']},
    description='',
    long_description=open('README.rst').read(),
)
