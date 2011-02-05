from chiplotle import *

plotter = instantiate_plotters( )[0]

for a in range(1,8):
   plotter.select_pen(a)
   e = Ellipse([5000,5000], 1000, 500, rotation = (10 * a))
   plotter.write(e)
 


