from chiplotle import *

def test_circle_01( ):
   c = Circle(0,0,400)
   assert c.format == 'PU0,0;CI400.0000,11;'

def test_circle_02( ):
   '''Filled circle formats correctly.'''
   c = Circle(0,0,400)
   c.filled = True
   assert c.format == 'PU0,0;WG400.0000,0.0000,359.0000,22.5000;'

