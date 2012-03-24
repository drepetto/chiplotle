from chiplotle import *
import os


def test_01():
   circ     = shapes.circle(100)
   filename = 'circle.hpgl'
   io.save_hpgl(circ, filename)

   assert os.path.exists(filename)

   os.remove(filename)
