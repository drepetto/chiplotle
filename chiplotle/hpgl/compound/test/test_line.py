from chiplotle import *

def test_line_01( ):
   t = Line((1, 2), (3, 4))

   assert t.xy == (1, 2)
   assert t.xy2 == (3, 4)
   assert t.format == 'PU;PA1,2;PD;PA3,4;PU;'


## parentage ##

def test_line_parentage_01( ):
   '''Line formats correctly with parent having `xy` be other than (0, 0).'''
   l = Line((1, 2), (3, 4))
   t = Container((3, 3), [l])

   assert l.xyabsolute == (4, 5)
   assert t.format == 'PU;PA4,5;PD;PA6,7;PU;'


