from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *

## No longer the case
# def test_hpglescape_escape_01( ):
#   '''The escape class attribute of _HPGLEscape commands can be set directly
#   from the instances.'''
#   on = On( )
#   off = Off( )
#   on.escape = chr(1)
#   assert on.escape == chr(1)
#   assert off.escape == chr(1)
#   off.escape = chr(2)
#   assert on.escape == chr(2)
#   assert off.escape == chr(2)
