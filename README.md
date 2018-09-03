# Chiplotle

[![CircleCI Status](https://circleci.com/gh/willprice/chiplotle.svg?style=shield)](https://circleci.com/gh/willprice/chiplotle)
[![Code coverage Status](https://codecov.io/gh/willprice/chiplotle/branch/master/graph/badge.svg)](https://codecov.io/gh/willprice/chiplotle)
[![Documentation Status](https://readthedocs.org/projects/chiplotle/badge/?version=latest)](https://chiplotle.readthedocs.io/en/latest/?badge=latest)
[![PyPI Version](https://badge.fury.io/py/Chiplotle.svg)](https://badge.fury.io/py/Chiplotle)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/ecede0d540c64622abab25fd79e8b74c)](https://www.codacy.com/app/will.price94/chiplotle?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=willprice/chiplotle&amp;utm_campaign=Badge_Grade)

**WARNING: This is a python 3 port WIP**, you should not use this fork until
this warning is removed.


Chiplotle is a Python library that implements and extends the HPGL
(Hewlett-Packard Graphics Language) plotter control language. It
supports all the standard HPGL commands as well as our own more complex
"compound HPGL" commands, implemented as Python classes. Chiplotle also
provides direct control of your HPGL-aware hardware via a standard
usb<->serial port interface.

Chiplotle has been tested with a variety of HPGL devices from various
companies, including Hewlett-Packard, Roland Digital Group, Houston
Instrument, etc. It includes plotter-specific configuration files for
many different plotter models, as well as a generic configuration that
should work with any HPGL-compliant device.

Chiplotle is written and maintained by Victor Adan and Douglas Repetto.

Find all there is to know about Chiplotle at:
http://music.columbia.edu/cmc/chiplotle
