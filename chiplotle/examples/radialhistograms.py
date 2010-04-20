from chiplotle import *

plotter = instantiate_plotters( )[0]

data = [0, .25, 1, .5, .7, 1, .2] * 3
rh_1 = RadialHistogramRF((0,0), 2000, 2500, data)
rh_1.fillines_spacing = 35 ## line spacing
rh_1.fill = True

data = [0, .25, 1, .5, .7, 1, .2] * 4
rh_2 = RadialHistogramLF((0,0), 2600, 3100, data)
rh_2.fillines_spacing = 0.01 ## angle in radians
rh_2.fill = True


#io.view([rh_1, rh_2])
plotter.write([rh_1, rh_2])
