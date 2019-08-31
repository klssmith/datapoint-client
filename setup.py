from setuptools import find_packages, setup

setup(
    name="datapoint-client",
    version="0.0.1",
    author="Katie Smith",
    description="A wrapper around the Met Office Datapoint API",
    url="https://github.com/klssmith/datapoint-client",
    packages=find_packages(),
    install_requires=["pytz", "requests"],
)
