from chiplotle import *
import math

plotter = instantiate_plotters( )[0]

count = 8
width = 400
height = 1000

triangles = [ ]
for i in range(count):
   a = i / float(count) * (math.pi * 2)
   r = 1000
   xy = mathtools.polar_to_xy(r, a)
   rotation = -a
   t = Isosceles(xy, width, height, rotation)
   triangles.append(t)

plotter.write(triangles)
