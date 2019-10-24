from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
import os


def test_01():
    circ = shapes.circle(100)
    filename = "circle"
    io.export(circ, filename, "png")

    assert os.path.exists(filename + ".png")

    os.remove(filename + ".png")
