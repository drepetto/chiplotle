from chiplotle import *
from py.test import raises

def test_groovyframe_01( ):
   '''
   GroovyFrame must be initialized with a pair of xy coordinates,
   a pair of width and height for square 1, a pair of width height
   coordinates for square 2 and line count scalar.
   '''
   t = GroovyFrame((0, 0), 100, 100, 110, 110, 4)
   assert t.w1 == 100
   assert t.h1 == 100
   assert t.w2 == 110
   assert t.h2 == 110
   assert t.lines_per_side == 4
   assert t.xy == (0, 0)


## scale ##

def test_groovyframe_scale_01( ):
   t = GroovyFrame((1, 2), 100, 100, 120, 120, 4)
   hpgltools.scale(t, 1.5)

   assert GroovyFrame._scalable == ['xy', 'w1', 'h1', 'w2', 'h2']
   assert t.xy == (1.5, 3)
   assert t.w1 == 150
   assert t.h1 == 150
   assert t.w2 == 180
   assert t.h2 == 180
