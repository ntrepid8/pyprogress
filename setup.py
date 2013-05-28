import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "pyprogress",
    version = "0.0.5",
    author = "Josh Austin",
    author_email = "josh.austin@gmail.com",
    description = ("A simple command line progress bar for python scripts."),
    license = "Apache 2.0",
    keywords = "progress bar command line",
    url = "https://github.com/ntrepid8/pyprogress",
    packages=['progress',],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: Apache 2.0 License",
    ],
)