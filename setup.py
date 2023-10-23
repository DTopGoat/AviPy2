from setuptools import find_packages, setup

with open("README.md") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="avpy",
    version="0.1.0",
    description="Package for aviation related tools",
    long_description=readme,
    author="Paolo Stet",
    url="https://github.com/pcs03/avpy",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
