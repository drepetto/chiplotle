from chiplotle import *

def main():
   number_size = 350
   line_spacing = number_size * 3.1

   plotter = instantiate_plotters( )[0]
   if not plotter:
      return None

   width = plotter.margins.soft.width
   height = plotter.margins.soft.height
   left = plotter.margins.soft.left 
   top = plotter.margins.soft.top - line_spacing

   numbers_per_line = width // 350
   r = [ ]
   for i in range(0, 401, 1):
      y = top - (i // numbers_per_line) * line_spacing
      x = left + (i % numbers_per_line) * number_size
      m = MayaNumber((x, y), i, number_size)
      m.filled = False
      r.append(m)
   plotter.write(r)


if __name__ == '__main__': main()
