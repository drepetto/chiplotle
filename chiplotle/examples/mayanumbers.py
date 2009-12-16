from chiplotle.utils.instantiate_plotter import instantiate_plotter
from chiplotle import MayaNumber

def main():
   numberSize = 350
   lineSpacing = numberSize * 3.1

   plotter = instantiate_plotter( )
   if not plotter:
      return None

   width = plotter.margins.soft.width
   height = plotter.margins.soft.height
   left = plotter.margins.soft.left 
   top = plotter.margins.soft.top - lineSpacing

   numbersPerLine = width // 350
   r = [ ]
   for i in range(0, 401, 1):
      y = top - (i // numbersPerLine) * lineSpacing
      x = left + (i % numbersPerLine) * numberSize
      m = MayaNumber((x, y), i, numberSize)
      m.filled = False
      r.append(m)
   plotter.write(r)


if __name__ == '__main__': main()
