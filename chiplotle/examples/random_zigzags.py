from chiplotle import *
import random

plotter = instantiate_plotter( )

plotter.selectPen(1)

for x in range(0, 1000, 10):
    y = random.randint(0, 1000)
    plotter.write(PD([x,y]))

plotter.selectPen(0)
