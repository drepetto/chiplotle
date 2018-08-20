from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.core.cfg.cfg import CONFIG_DIR
from chiplotle.tools.io.export import export
from chiplotle.tools.io._open_file import _open_file
import os
import time

def view(expr, fmt='eps'):
    '''Displays Chiplotle-HPGL objects for prevewing.

    - `expr` can be an iterable (e.g., list) or a Chiplotle-HPGL object.
    - `fmt` is the file format to which the given `expr` will be
        converted for viewing. The default is 'eps'.
    '''

    outdir    = os.path.join(CONFIG_DIR, 'output')
    filename = time.strftime('%Y%m%d_%H%M%S')
    filepath = os.path.join(outdir, filename)
    imgfile  = export(expr, filepath, fmt)

    ## show!
    _open_file(imgfile)
