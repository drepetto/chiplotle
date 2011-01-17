from chiplotle import *

## coordinate attributes ##

def test_hpglcompounddecorator_10( ):
   '''The coordinate values of a wrapped shape are acessed correctly.'''
   s = Circle((1, 2), 100)
   t = DPen(s, 1)
   assert t.xy == Vector(1, 2)
   assert t.x == 1
   assert t.y == 2


def test_hpglcompounddecorator_11( ):
   '''The coordinate values xy of a wrapped shape can be set.'''
   s = Circle((1, 2), 100)
   t = DPen(s, 1)
   t.xy = (3, 4)
   assert t.xy == Vector(3, 4)
   assert t.x == 3
   assert t.y == 4


def test_hpglcompounddecorator_12( ):
   '''The coordinate value x of a wrapped shape can be set.'''
   s = Circle((1, 2), 100)
   t = DPen(s, 1)
   t.x = 3
   assert t.xy == Vector(3, 2)
   assert t.x == 3
   assert t.y == 2


def test_hpglcompounddecorator_13( ):
   '''The coordinate value x of a wrapped shape can be set.'''
   s = Circle((1, 2), 100)
   t = DPen(s, 1)
   t.y = 3
   assert t.xy == Vector(1, 3)
   assert t.x == 1
   assert t.y == 3


