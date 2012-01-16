from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.path import Path
from chiplotle.tools.mathtools.bezier_interpolation import bezier_interpolation


def bezier_path(points, curvature, interpolation_count = 50):
   '''Returns a Path with bezier interpolation between the given `points`.
   The interpolation is computed so that the resulting path touches the 
   given points.
   
   - `points` the key points from which to interpolate.
   - `curvature` the smoothness of the curve [0, 1].
   - `interpolation_count` is the number of points to add by interpolation,
      per segment.
   '''

   if not (0 <= curvature <= 1):
      raise ValueError('`curvature` must be between 0 and 1 inclusive.')

   if curvature == 0:
      return Path(points)

   ## else we have a curve...
   points = CoordinateArray(points)

   curvature = 4 + (1.0 - curvature) * 40
   bi = [0, -0.25]
   a = [Coordinate(0, 0), (points[2] - points[0] - Coordinate(0, 0)) / 4.0]

   ## compute bi and a...
   for i in range(2, len(points)-1):
      bi.append(-1 / (curvature + bi[i - 1]))
      a.append(-(points[i+1] - points[i-1] - a[i-1]) * bi[i])

   ## compute dxy...
   dxy = [Coordinate(0, 0)]
   for i in reversed(range(len(points) - 1)):
      dxy.insert(0, a[i] + dxy[0] * bi[i])
 
   ## compute interpolated points...
   plot_points = [ ]
   for i in range(len(points) - 1):
      control_points = [
         points[i], 
         points[i] + dxy[i], 
         points[i+1] - dxy[i+1], 
         points[i+1]]
      plot_points += bezier_interpolation(control_points, 
                                          interpolation_count, 1)[:-1]

   return Path(plot_points)



## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.geometry.core.path import Path
   from chiplotle.geometry.core.group import Group
   from chiplotle.tools import io
   points  = [(0, 0), (1000, 1000), (-1000, 1000), (-1000, -1000), (1000, -1000), (0, 0)]
   e1 = bezier_path(points, 1)
   e2 = bezier_path(points, 0.5)
   e3 = bezier_path(points, 0)
   assert isinstance(e1, Path)

   io.view(Group([e1, e2, e3]))
