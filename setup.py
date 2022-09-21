"""Python setup.py for python_nogil_benchmark package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("python_nogil_benchmark", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="python_nogil_benchmark",
    version=read("python_nogil_benchmark", "VERSION"),
    description="Awesome python_nogil_benchmark created by gavincyi",
    url="https://github.com/gavincyi/python-nogil-benchmark/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="gavincyi",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["python_nogil_benchmark = python_nogil_benchmark.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
