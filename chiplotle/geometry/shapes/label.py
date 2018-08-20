from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.geometry.core.label import Label

def label(text,
            charwidth,
            charheight,
            charspace = None,
            linespace = None,
            origin = 'bottom-left'):
    return Label(text, charwidth, charheight, charspace, linespace, origin)
