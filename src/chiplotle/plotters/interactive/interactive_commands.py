"""
Interactive plotter routines.

Note that these routines may not work on your plotter. They are
known to work on most HP and Roland plotters, but they do NOT
work on the Houston Instruments DMP-60 (and probably other Houston
Instruments plotters). This is because the DMP-60 interprets manual
pen moves as attempts to reset the origin, which interferes with
these routines.
"""


from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from __future__ import absolute_import
from builtins import int
from builtins import input
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.hpgl.commands import SC, IP, IW


def interactive_set_plot_window(plotter):
    """
    Interactive routine to manually move the pen to set the margins of the plotting window.
    """

    plotter.write(IP())
    plotter.write(IW())
    # plotter.write(SC())

    print("Interactive set plot window:")
    print("Move pen to lower left and press enter.")
    input()
    position = plotter.actual_position[0]
    x1 = position.x
    y1 = position.y

    print("Move pen to upper right and press enter.")
    input()
    position = plotter.actual_position[0]
    x2 = position.x
    y2 = position.y

    plotter.set_plot_window(Coordinate(x1, y1), Coordinate(x2, y2))

    """
from chiplotle.plotters.interactive.interactive_commands import *
interactive_set_plot_window(plotter)
    """


def interactive_set_plot_window_and_units(plotter):
    """
    User sets window size and then defines units inside of that window.

    Example:

        >>> from chiplotle.interactive.interactive_commands import *
        >>> interactive_set_plot_window_and_units(plotter)
    """
    plotter.write(IP())
    plotter.write(IW())
    plotter.write(SC())

    interactive_set_plot_window(plotter)

    print("Enter value for left side (typically 0):")
    left = int(input())
    print("Enter value for bottom side (typically 0):")
    bottom = int(input())
    print("Enter value for right side (width of plot in your units):")
    right = int(input())
    print("Enter value for top side (height of plot in your units):")
    top = int(input())

    plotter.write(SC([left, right, bottom, top]))
    print("new soft margins:")
    print(plotter.margins.soft)


def interactive_set_plot_window_auto_units(plotter):
    """
    User sets window size and then units are automatically set
    to user's choise of inches, millimeters, or centimeters.

    Example:

        >>> from chiplotle.plotters.interactive.interactive_commands import *
        >>> interactive_set_plot_window_auto_units(plotter)
    """
    plotter.write(IP())
    plotter.write(IW())
    plotter.write(SC())

    interactive_set_plot_window(plotter)

    orig_right = plotter.margins.soft.right
    orig_top = plotter.margins.soft.top

    width = plotter.margins.soft.width
    height = plotter.margins.soft.height

    inches_w = width / 1016.0
    inches_h = height / 1016.0

    cm_w = width / 400.0
    cm_h = height / 400.0

    mm_w = width / 40.0
    mm_h = width / 40.0

    print("Window size is:")
    print("%f inches x %f inches" % (inches_w, inches_h))
    print("%f cm x %f cm" % (cm_w, cm_h))
    print("%f mm x %f mm" % (mm_w, mm_h))

    print("Choose units:")
    print("1) inches")
    print("2) cm")
    print("3) mm")

    units = int(input())

    left = plotter.margins.soft.left
    bottom = plotter.margins.soft.bottom

    if units == 1:
        right = left + 1016
        top = bottom + 1016
    elif units == 2:
        right = left + 400
        top = bottom + 400
    elif units == 3:
        right = left + 40
        top = righ + 40
    else:
        print("That wasn't one of the choices!")
        return

    plotter.write(IP([left, bottom, right, top]))
    plotter.write(SC([0, 1, 0, 1]))
    # plotter.write(IP([left, bottom, orig_right, orig_top]))

    # These margins will be WRONG!!! They'll be the floor integer margins,
    # not the margins set via the set_plot_window() above. ARRRRG!
    print("new soft margins:")
    print(plotter.margins.soft)
