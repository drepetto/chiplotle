from chiplotle import *


p1 = Path([(0, 0), (0, 2000), (2000, 2000), (2000, 0), (0,0)], curvature=0)
p2 = Path([(0, 0), (0, 2000), (2000, 2000), (2000, 0), (0,0)], curvature=0.5)
p3 = Path([(0, 0), (0, 2000), (2000, 2000), (2000, 0), (0,0)], curvature=1)

print p1.points

plotter = instantiate_plotters( )[0]
plotter.write([p1, p2, p3])


