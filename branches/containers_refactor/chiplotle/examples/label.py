from chiplotle import *


labels = [ ]
rects = [ ]
spacing = 500
for i in range(1, 10):
   r = Cross((0, spacing * i), width = 100, height = 100)
   rects.append(r)
   l = Label((0, spacing * i), 'Label with origin %s.' %i, pen=1)
   l.origin = i
   l.charsize = (0.5, .5)
   labels.append(l)

result = rects + labels

io.view(result)

plotter = instantiate_plotters( )[0]
plotter.write(result)

