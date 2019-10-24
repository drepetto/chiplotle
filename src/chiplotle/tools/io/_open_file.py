from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
import os
import sys


def _open_file(file_name, application=None):
    """Generic cross-platform file opener.

    - `file_name` is the file to open, including path.
    - `application` is the application to use to open the file;
        must be a string or None. If not given, the function will use a
        generic OS dependent file openner.
    """

    if os.name == "nt":
        os.startfile(file_name)
    else:
        if sys.platform.lower().startswith("linux"):
            viewer = application or "xdg-open"
        else:
            viewer = application or "open"
        os.system("%s %s &" % (viewer, file_name))
