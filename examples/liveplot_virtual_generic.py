#!/usr/bin/env python

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter

"""
Demonstrates the use of a virtual plotter with the generic plotter.
Paper will automatically be set to 8.5x11" (ANSI A).

You must have hp2xx installed for io.view() to work!
"""

plotter = instantiate_virtual_plotter()

plotter.margins.soft.draw_outline()
plotter.goto_center()
plotter.select_pen(1)
plotter.write(hpgl.CI(1000))
plotter.select_pen(2)
plotter.write(hpgl.CI(500))
plotter.select_pen(3)
plotter.write(hpgl.CI(250))
plotter.select_pen(4)
plotter.write(hpgl.CI(125))

io.view(plotter)
