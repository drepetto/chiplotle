from chiplotle import *


def test_rectangle_01( ):
   r = Rectangle((0, 0), 10, 20)
   
   assert r.xy == (0, 0)
   assert r.width == 10
   assert r.height == 20


def test_rectangle_scale_01( ):
   t = Rectangle((1, 2), 10, 20)
   hpgltools.scale(t, 1.5)

   assert Rectangle._scalable == ['xy', 'width', 'height']
   assert t.xy == (1.5, 3)
   assert t.width == 15
   assert t.height == 30
   
