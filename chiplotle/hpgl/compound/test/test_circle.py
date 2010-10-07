from chiplotle import *

def test_circle_01( ):
   c = Circle((0,0),400)
   assert c.format == 'PU;PA0,0;CI400.00;'

def test_circle_02( ):
   '''Filled circle formats correctly.'''
   c = Circle((0,0),400)
   c.filled = True
   assert c.format == 'PU;PA0,0;WG400.00,0.00,359.00;'


## scale ##

def test_circle_scale_01( ):
   c = Circle((1, 2), 100)
   hpgltools.scale(c, 1.5)

   assert Circle._scalable == ['xy', 'radius']
   assert c.radius == 150
   assert c.xy == (1.5, 3)


## transpose ##

def test_circle_transpose_01( ):
   c = Circle((1, 2), 100)
   hpgltools.transpose(c, (2, 1))

   assert c.radius == 100
   assert c.xy == (3, 3)
