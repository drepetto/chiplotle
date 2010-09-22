from chiplotle import *
import Image

'''
This script converts an image into a grid of concentric circles. The diameter of these circles is proportional to the darkness of the pixels in the image. 
Each pixel is mapped to a set of concentric circles. 
'''

def circleize_image(image, cell_size=390):
   '''Returns a list of Circle instances.'''
   hpgl = [ ]
   width = image.size[0]
   for i, point in enumerate(image.getdata( )):
      point = (255.0 - point) / 255.0
      x = (i % width) * cell_size
      y = (i // width) * cell_size

      if point > 0.001:
         circle_count = int(point * 4)
         for n in range(1, circle_count + 1):
            #radius = (point / n) ** 1.5 * cell_size / 1.5
            radius = (point / circle_count * n) ** 2.2 * cell_size / 1.26
            hpgl.append(Circle((y, x), radius, chord = 22, pen=1))

   return Container((200, 200), hpgl)


if __name__ == '__main__':
   ## open and resize image...
   image = Image.open('media/douglas_repetto.jpg').convert('L')
   size = image.size
   size_ratio =  size[0] / float(size[1])
   width = 70
   thumb = image.resize((width, int(round(width / size_ratio))), 
      Image.ANTIALIAS)
   #thumb.show( )
   print 'image size:', thumb.size
   ## convert image to HPGL art...!
   retrato = circleize_image(thumb, 150)
   io.view(retrato)
   plotter = instantiate_plotters( )[0]
   plotter.write(retrato)
