from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.tools.geometrytools.get_minmax_coordinates \
   import get_minmax_coordinates

def get_radius(shape):
   '''
   
   Returns the distance from the center of the shape to the most distant edge.
   If the shape is a circle, this will be the radius. If it is some other shape
   then the meaning of the returned value is undefined. 
   
   '''
   
   bounds = get_minmax_coordinates(shape.points)
   w, h = bounds[1] - bounds[0]
   return max(w, h) / 2.0
   


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.shapes.circle import circle
   from chiplotle.geometry.transforms.noise import noise
   from chiplotle.geometry.transforms.offset import offset
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io

   c1 = circle(1000)
   r1 = get_radius(c1)

   c2 = circle(1000)
   noise(c2, 500)
   r2 = get_radius(c2)
   
   c3 = circle(1000)
   offset(c3, (250, 250))
   r3 = get_radius(c3)
   
   g = Group([c1, c2, c3])
   
   print "r1: %f r2: %f r3: %f" % (r1, r2, r3)
   
   io.view(g)
   
