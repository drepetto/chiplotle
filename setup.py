#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup, find_packages


about = dict()
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "src", "chiplotle", "__version__.py"), "r") as f:
    exec(f.read(), about)


setup(
    name=about["__title__"],
    version=about["__version__"],
    description=about["__description__"],
    long_description=about["__description__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    url=about["__url__"],
    keywords=["vector", "graphics", "hpgl", "plotter", "plot", "pen"],
    license=about["__license__"],
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Intended Audience :: Developers',
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
    ],
    # XXX: UNUSURE
    packages=find_packages("src"),
    # XXX: UNUSURE
    #include_package_data=True,
    # XXX: UNUSURE
    package_dir={'': 'src'},
    install_requires=[
        "pyserial<=3",
        "numpy<=2",
        "future>=0.16.0"
    ],
    entry_points={
        "console_scripts": [
            "chiplotle = chiplotle.core.cfg._run_chiplotle:_run_chiplotle"
        ]
    },
    scripts=[
        "src/chiplotle/scripts/envelope.py",
        "src/chiplotle/scripts/find_hpgl_file_dimensions.py",
        "src/chiplotle/scripts/plot_hpgl_file_max_size.py",
        "src/chiplotle/scripts/plot_hpgl_file.py",
        "src/chiplotle/scripts/plot_hpgl_file_virtual.py",
        "src/chiplotle/scripts/typewriter.py",
        "src/chiplotle/scripts/view_hpgl_file.py",
    ],
)
