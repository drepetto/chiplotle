from chiplotle import *

def test_PA_01( ):
   t = PA( )

   assert t.xy == [ ]
   assert isinstance(t.xy, CoordinateArray)
   assert t.format == 'PA;'


## eq ##

def test_PA__eq__01( ):
   assert PA((1,2,3,4)) == PA((1,2,3,4))

