from chiplotle import *
from chiplotle.geometry import *

f1 = fan(1000, 0, 3.14/4., 500)
f2 = fan(1000, 3.1415/2, 3.14/8., 500)

pole = circle(100)

t = Group([pole, f1, f2])

io.view(t)
