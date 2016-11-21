import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="Archey3",
    version="0.6",
    author="Gabriel Simmer",
    author_email="bladesimmer@gmail.com",
    description="Archey3 fork with lockscreen & more supported distros.",
    license="GPL",
    url="http://bluepeppers.github.com/archey3",
    long_description=read("README.md"),
    scripts=["archey3"]
)
