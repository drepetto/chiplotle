from chiplotle import *
from chiplotle.utils.run_chiplotle_UNIX import plotter

plotter.selectPen(1)
plotter.write(PU([100,100]))
plotter.write(PD([200,100]))
plotter.write(PD([200,200]))
plotter.write(PD([100,200]))
plotter.write(PD([100,100]))
plotter.selectPen(0)


