from chiplotle import *
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.shapes.ellipse import ellipse
from chiplotle.geometry.transforms.rotate import rotate

import math

two_pi = math.pi * 2.0

g = []

for a in range(0,7):
   e = ellipse(5000, 1000, 500)
   rotate(e, (two_pi / 7) * a)
   g.append(e)
   
io.view(Group(g))

