from chiplotle import *
from chiplotle.utils.instantiate_plotter import instantiate_plotter

plotter = instantiate_plotters( )[0]
if plotter:

   def test_circle_plot_01( ):
      '''Radius.'''
      rs = range(1, 10)

      result = [ ]
      for r in rs:
         r *= 100
         result.append(Circle((0, 0), r, pen = 1))

      plotter.write(result)


   def test_circle_plot_02( ):
      '''Position and fill.'''
      px = range(1, 8)
      py = range(1, 4)
      margins = plotter.margins.soft
      result =  [ ]
      for x in px:
         x *= 200
         x += margins.left / 2.
         for i, y in enumerate(py):
            y *= 200
            y += margins.top / 2.
            result.append(Circle((x, y), 100, pen = 1, filled = bool(i % 2)))

      plotter.write(result)

