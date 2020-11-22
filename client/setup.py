from setuptools import find_packages, setup

with open('./requirements.txt', 'r') as f:
    requirements = f.read().splitlines()

setup(
    name = "counting",
    version = "0.1",
    description = "Client Library for Counting Stars API",
    packages = find_packages(),
    install_requires = requirements
)