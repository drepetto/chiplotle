from chiplotle import *

def test_rectangle_01( ):
   r = Rectangle(5, 10, 10, 20)
   assert r.format == 'PU;PA0.0,20.0;PD;PA10.0,20.0;PA10.0,0.0;PA0.0,0.0;PA0.0,20.0;PU;'

