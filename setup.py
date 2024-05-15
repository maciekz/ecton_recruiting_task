import os

from setuptools import setup


def read(file_name):
    return open(os.path.join(os.path.dirname(__file__), file_name)).read()


setup(
    name="ecton_recruiting_task",
    version="1.0",
    author="Maciej Zięba",
    author_email="maciekz82@gmail.com",
    description="Ecton Recruiting Task",
    url="https://github.com/maciekz/ecton_recruiting_task",
    long_description=read("README.md"),
    entry_points={},
    install_requires=[
        "PyYAML == 6.0.1",
        "pytest == 8.2.0",
    ],
    extras_require={
        "dev": [
            "black",
        ]
    },
)