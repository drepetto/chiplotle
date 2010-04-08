from chiplotle import *
from py.test import raises

def test_groovyframe_01( ):
   '''
   GroovyFrame must be initialized with a pair of xy coordinates,
   a pair of width and height for square 1, a pair of width height
   coordinates for square 2 and line count scalar.
   '''
   t = GroovyFrame((0, 0), (100, 100), (110, 110), 4)
   assert t.wh1 == (100, 100)
   assert t.wh2 == (110, 110)
   assert t.lines_per_side == 4
   assert t.xy == (0, 0)

def test_groovyframe_02( ):
   '''Width and height of rectangles must be a pair.'''
   assert raises(AssertionError, 't = GroovyFrame((0, 0), 100, 110, 4)')
   assert raises(AssertionError, 't=GroovyFrame((0, 0), 100, (110, 110), 4)')
   assert raises(AssertionError, 't=GroovyFrame((0, 0), (100, 100), 110, 4)')
