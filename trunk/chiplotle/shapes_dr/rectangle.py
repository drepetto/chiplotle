from chiplotle.shapes.polygon import Polygon
from chiplotle.geometry.coordinate import Coordinate
from chiplotle.hpgl.commands import PU, PD, PA

class Rectangle(Polygon):
   '''
      A rectangle with a width, height, and offset.
      
      offset is a Coordinate for moving the Rectangle around on the page.
      
      The Rectangle is drawn with the current pen location as the center.
      offset may be used to shift this around, for example, to draw from
      the lower, left corner.
   '''

   def __init__(self, width, height, offset):  
      self.width = width
      self.heigth = height
      
      corners = []
      corners.append(Coordinate(-width/2, -height/2))
      corners.append(Coordinate(-width/2, height/2))
      corners.append(Coordinate(width/2, height/2))
      corners.append(Coordinate(width/2, -height/2))
      Polygon.__init__(self, [corners], offset)  
      
   


if __name__ == '__main__':
   from chiplotle.shapes.rectangle import Rectangle
   from chiplotle import io
   r1 = Rectangle(1000,2000, [0,0])
   print r1.points
   print r1.format
   io.view(r1)
   
   raw_input()

   ## [VA] this is a weird artefact of Rectangle inheriting from Polygon...
   r1.point_lists.append([Coordinate(0, 0), Coordinate(300, 400)])
   print '\nNo longer a square!'
   print r1.points
   print r1.format
   io.view(r1)

   raw_input()