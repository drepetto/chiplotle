from chiplotle import *
import random

plotter = instantiate_plotters( )[0]

plotter.select_pen(1)

result = [ ]
for x in range(0, 1000, 10):
   y = random.randint(0, 1000)
   result.append(PD([x, y]))

plotter.write(result)

plotter.select_pen(0)
