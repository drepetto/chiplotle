#!/usr/bin/env python

from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter

'''
Demonstrates the use of a virtual plotter with a specific plotter definition.

You must have hp2xx installed for io.view() to work!
'''

'''
    compute size of paper:
    there are 40 plotter units per mm
    HP7550A reference lists 11x17 (ANSI B) max plot dimensions as:
    254 x 411mm
'''

paper_width = 411 * 40
paper_length = 254 * 40

plotter = instantiate_virtual_plotter(type="HP7550A", 
    left_bottom = Coordinate(0,0), 
    right_top = Coordinate(paper_width, paper_length) )

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

