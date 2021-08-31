# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
# Copyright © 2021, Spyder Pomodoro Timer
#
# Licensed under the terms of the MIT license
# ----------------------------------------------------------------------------
"""
Spyder Pomodoro Timer setup.
"""
from setuptools import find_packages
from setuptools import setup

from spyder_pomodoro_timer import __version__


setup(
    # See: https://setuptools.readthedocs.io/en/latest/setuptools.html
    name="spyder-pomodoro-timer",
    version=__version__,
    author="Spyder Pomodoro Timer",
    author_email="fpalm@qu4nt.com",
    description="A very simple pomodoro timer that shows in the status bar.",
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
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Topic :: Scientific/Engineering",
    ],
)
