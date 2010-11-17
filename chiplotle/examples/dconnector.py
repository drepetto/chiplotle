from chiplotle import *
from random import randint

'''The DConnector draws connecting lines between shapes in a Group.'''

plotter = instantiate_plotters( )[0]


shapes = [ ]
for i in range(4):
   shapes.append(Circle((randint(-4000, 4000), randint(-4000, 4000)), 300))

dc = DConnector(shapes, True)

plotter.write(VS(8))
plotter.write(dc)
