from chiplotle import *

plotter = instantiate_plotters( )[0]

line = Path([(0, 0), (1000, 1000), (-1000, 1000), (0, 2000)], 1)
arrow = DArrow(line, 500, 1000)

io.view(arrow)
#plotter.write(arrow)

