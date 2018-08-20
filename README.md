# Chiplotle

[![CircleCI](https://circleci.com/gh/willprice/chiplotle.svg?style=svg)](https://circleci.com/gh/willprice/chiplotle)

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
