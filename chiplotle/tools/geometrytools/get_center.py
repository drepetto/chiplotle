from chiplotle.geometry.coordinate import Coordinate
from chiplotle.tools.geometrytools.get_bounding_coordinate_pairs import get_bounding_coordinate_pairs

def get_center(shape):
   '''
   
   Returns a Coordinate() that is in the center of the shape.
   "center" is defined as being half way between the top/bottom
   and left/right-most points. This will be different from the
   centroid, which takes the distribution of the points into
   consideration.
   
   '''
   
   bounds = get_bounding_coordinate_pairs(shape)
   
#   dist_w = bounds[1][0] - bounds[0][0]
#   dist_h = bounds[1][1] - bounds[0][1]
#
#   x_center = bounds[0][0] + (dist_w/2.0)
#   y_center = bounds[0][1] + (dist_h/2.0)
   
   w, h = bounds[1] - bounds[0]
   x_center = bounds[0].x + (w / 2.0)
   y_center = bounds[0].y + (h / 2.0)

   return Coordinate(x_center, y_center)
   


## DEMO
if __name__ == '__main__':
   from chiplotle.geometry.factory.circle import circle
   from chiplotle.geometry.destructive_transforms.noise import noise
   from chiplotle.geometry.destructive_transforms.offset import offset
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io

   c1 = circle(1000)
   center1 = get_center(c1)

   c2 = circle(1000)
   noise(c2, 500)
   center2 = get_center(c2)
   
   c3 = circle(1000)
   offset(c3, (250, 250))
   center3 = get_center(c3)
   
   g = Group([c1, c2, c3])
   
   print center1
   print center2
   print center3
   
   io.view(g)
   
