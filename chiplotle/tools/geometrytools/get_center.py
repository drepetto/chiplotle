from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.tools.geometrytools.get_minmax_coordinates \
   import get_minmax_coordinates

def get_center(coords):
   '''
   
   Returns a Coordinate() that is in the center of the given
   set/list of `coords`.
   "center" is defined as being half way between the top/bottom
   and left/right-most points. This will be different from the
   centroid, which takes the distribution of the points into
   consideration.
   
   '''
   
   bounds = get_minmax_coordinates(coords)
   
   w, h = bounds[1] - bounds[0]
   x_center = bounds[0].x + (w / 2.0)
   y_center = bounds[0].y + (h / 2.0)

   return Coordinate(x_center, y_center)
   

