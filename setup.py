"""distribution via PyPi."""

import setuptools
from darkseed.version import __version__

with open('README.rst', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name='darkseed',
    version=__version__,
    author='Tom Spalding',
    author_email='tom@blackforestbotanics.com',
    description='a Pelican theme for the Botanixxx blog.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/x-rst',
    url='https://github.com/blackforestbotanics/darkseed',
    packages=setuptools.find_packages(),
    license='MIT',
    classifiers=[
        'Framework :: Pelican :: Themes',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
