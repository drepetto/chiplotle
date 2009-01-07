from chiplotle import *

def test_circle_01( ):
   c = Circle(0,0,400)
   assert c.format == 'PU0.0,0.0;CI400.0;'

def test_circle_02( ):
   '''Filled circle formats correctly.'''
   c = Circle(0,0,400)
   c.filled = True
   assert c.format == 'PU0.0,0.0;WG400.0,0,359;'

