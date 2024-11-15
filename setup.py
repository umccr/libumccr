# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Note:
#   Version scheme follow PEP440 https://peps.python.org/pep-0440/
#   _NOT_ SemVer https://semver.org

setup(
    name="libumccr",
    version="0.4.1",
    author="UMCCR and Contributors",
    author_email="services@umccr.org",
    description="UMCCR Reusable Python modules",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/umccr/libumccr",
    license="MIT",
    packages=find_packages(exclude=("tests**", "docs")),
    project_urls={
        "Bug Tracker": "https://github.com/umccr/libumccr/issues",
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    extras_require={
        "dev": [
            "pipdeptree",
            "twine",
            "setuptools",
            "wheel",
            "build",
            "pdoc3",
            "pre-commit",
            "detect-secrets",
        ],
        "test": [
            "pytest",
            "pytest-cov",
            "flake8",
            "mockito",
            "tox",
            "nose2",
            "awscli-local",
            "cachetools",
        ],
        "libgdrive": [
            "requests",
            "pandas",
            "gspread",
            "gspread-pandas",
            "google-auth",
            "cachetools",
        ],
        "aws": [
            "boto3",
            "botocore",
            "cachetools",
        ],
        "all": [
            "Django",
            "boto3",
            "botocore",
            "cachetools",
            "requests",
            "pandas",
            "gspread",
            "gspread-pandas",
            "google-auth",
        ],
    },
    install_requires=[
        # silent night
    ],
)
