from chiplotle.utils.run_chiplotle_UNIX import p
from chiplotle import MayaNumber

def main():
   numberSize = 350
   lineSpacing = numberSize * 3.1

   width = p.marginSoft.width
   height = p.marginSoft.height
   left = p.marginSoft.left 
   top = p.marginSoft.top - lineSpacing

   numbersPerLine = width // 350
   r = [ ]
   for i in range(0, 401, 1):
      y = top - (i // numbersPerLine) * lineSpacing
      x = left + (i % numbersPerLine) * numberSize
      m = MayaNumber(x, y, i, numberSize)
      m.filled = False
      r.append(m)
   p.write(r)


if __name__ == '__main__': main()
