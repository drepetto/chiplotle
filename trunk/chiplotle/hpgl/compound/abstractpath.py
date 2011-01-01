from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.geometry.coordinatearray import CoordinateArray


class _AbstractPath(_HPGLCompoundShape):
   '''Abstract class for path-like classes.

      - `points` is the list of control points.
      - `interpolation_count` detrmines the number of points calculated for 
         each curve segment. i.e., every point pair.
   '''

   _scalable = _HPGLCompoundShape._scalable + ['points']

   def __init__(self, points, interpolation_count=None, xy=None):
      self.points = points
      self.interpolation_count = interpolation_count or 50
      xy = xy or (0, 0)
      _HPGLCompoundShape.__init__(self, xy) 


   ## PROPERTIES ##

   @apply
   def points( ):
      def fget(self):
         return self._points
      def fset(self, arg):
         ## TODO: check that there are at least three points.
         self._points = CoordinateArray(arg)
      return property(**locals( ))

