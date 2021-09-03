# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Francisco Palm
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_pomodoro_timer import __version__

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-pomodoro-timer",
    version=__version__,
    author="Francisco Palm",
    author_email="fpalm@qu4nt.com",
    description="A very simple pomodoro timer that shows in the status bar.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    license="MIT license",
    url="https://github.com/map0logo/spyder-pomodoro-timer",
    python_requires='>= 3.7',
    install_requires=[
        "qtpy",
        "qtawesome",
        "spyder>=5.0.1",
    ],
    packages=find_packages(),
    entry_points={
        "spyder.plugins": [
            "spyder_pomodoro_timer = spyder_pomodoro_timer.spyder.plugin:SpyderPomodoroTimer"
        ],
    },
    classifiers=[
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Scientific/Engineering",
        "Topic :: Utilities"
    ],
)
