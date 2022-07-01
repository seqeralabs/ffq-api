from setuptools import setup

with open("VERSION", "r") as fh:
    version = fh.read()

setup(
    version=version
)
