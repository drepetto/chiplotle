from chiplotle import *
import os


def test_01():
   circ     = shapes.circle(100)
   filename = 'circle'
   io.export(circ, filename, 'png')

   assert os.path.exists(filename + '.png')

   os.remove(filename + '.png')
