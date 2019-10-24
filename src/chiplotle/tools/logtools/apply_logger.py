from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.tools.logtools.get_logger import get_logger


def apply_logger(f):
    """Applies a logger object to the 'wrapped' function."""
    logger = get_logger(f.__name__)
    f.logger = logger
    return f
