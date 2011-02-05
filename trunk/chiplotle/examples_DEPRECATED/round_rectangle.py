from chiplotle import *

r = RoundRectangle((-500, 500), 1000, 2000, weight=3)

plotter = instantiate_plotters( )[0]
plotter.write(r)


