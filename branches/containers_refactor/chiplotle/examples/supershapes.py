from __future__ import division
from chiplotle import *

plotter = instantiate_plotters( )[0]

width = plotter.margins.soft.width * 3. / 4.
height = plotter.margins.soft.height * 3. / 4.
left = plotter.margins.soft.left
top = plotter.margins.soft.top

result = [ ]
cols = 10
rows = 8
for i in range(1, cols + 1):
   x = i * width / cols
   x += left
   for j in range(1, rows + 1):
      y = -j * height / rows
      y += top
      b = Supershape((x, y), width / cols / 4, width / cols / 4, 5, 
         3.3, i, j, b=.75, range=4*3.1416, points=200)
      result.append(b)      


#io.view(result)
plotter.select_pen(1)
plotter.write(result)
plotter.select_pen(0)
