from chiplotle import *

f1 = Fan((0,0), 1000, 0, 3.14/4., 500)
f2 = Fan((0,0), 1000, 3.1415/2, 3.14/8., 500)

pole = Circle((0,0), 100)

t = Group((1000,1000), [pole, f1, f2])
t.pen = 1

io.view(t)
