from chiplotle import *

bc = BooleanCycle((0, 1000), 1000, [1,0,1,1,0,0,1,0], 100)

plotter = instantiate_plotters( )[0]

plotter.write(bc)
