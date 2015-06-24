from distutils.core import setup
from setuptools import setup, find_packages

setup(
    name='floccus',
    version="0.0.1",
    author='Oliver Keyes',
    author_email='ironholds@gmail.com',
    url='https://github.com/Ironholds/floccus',
    license=open('LICENSE').read(),
    description='A set of utilities for handling CirrusSearch log data',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Text Processing :: General",
        "Topic :: Utilities",
        "Topic :: Scientific/Engineering"
    ],
)
