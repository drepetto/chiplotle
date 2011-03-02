from chiplotle import *
from chiplotle.geometry.core.path import Path
from chiplotle.geometry.shapes.arrow import arrow

line = Path([(0, 0), (1000, 1000), (-1000, 1000), (0, 2000)])
a = arrow(line, 500, 1000)

io.view(a)
