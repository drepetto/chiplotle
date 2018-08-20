from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle import *
from chiplotle.hpgl.commands import PA

def test_PA_01( ):
    t = PA( )

    assert t.xy == CoordinateArray([ ])
    assert isinstance(t.xy, CoordinateArray)
    assert t.format == 'PA;'


## eq ##

def test_PA__eq__01( ):
    assert PA([(1,2),(3,4)]) == PA([(1,2),(3,4)])

