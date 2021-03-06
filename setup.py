from setuptools import setup, find_packages
from os import path
from setuptools.extension import Extension


here = path.abspath(path.dirname(__file__))


setup(
    name = "fzfopen",

    version = "0.0",

    description = "Search and open files using fzf",

    author = "H. Onur Solmaz",

    author_email = "onursolmaz@gmail.com",

    packages = find_packages(exclude=["contrib", "docs", "tests"]),

    extras_require = {
        "dev": ["check-manifest"],
        "test": ["coverage"],
    },

    entry_points = {
        "console_scripts": [
            "fzfopen_find=fzfopen.main:fzfopen_find",
            "fzfopen_locate=fzfopen.main:fzfopen_locate",
            "fzfopen=fzfopen.main:fzfopen",
        ],
    },
)



