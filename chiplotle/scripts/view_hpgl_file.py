#!/usr/bin/env python
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.tools import *
import sys
import time


def view_hpgl(file):
    """Convert hpgl to eps and view with default system eps app."""
    f = io.import_hpgl_file(file)
    io.view(f)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Must give HPGL file to view.\nExample: $ view_hpgl myfile.hpgl")
        sys.exit(2)
    file = sys.argv[1]

    view_hpgl(file)
