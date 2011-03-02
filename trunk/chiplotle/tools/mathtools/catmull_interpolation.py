from chiplotle.geometry.core.coordinatearray import CoordinateArray

def catmull_interpolation(control_points, points_to_compute):
      '''Computes Catmull-Rom interpolations from given `control_points`.
      first and last point are not on the curve, but define
      initial and final tangent
      - `control_points` : A list of (x, y) control points.
      - `points_to_compute`: An int of the number of points to compute.
      '''

      ## TODO: move 'spline' out of this function?
      def spline(p_1, p0, p1, p2, t):
         point = ((2 * t**2 - t**3 - t) * p_1 + 
            (3 * t**3 - 5 * t**2 + 2) * p0 + 
            (4 * t**2 -3 * t**3 + t) * p1 + 
            (t**3 - t**2) * p2) * 0.5
         return point

      try: ## use numpy for speed...
         import numpy
         p_array = numpy.array(control_points)
      except ImportError:
         p_array = CoordinateArray(control_points)

      p_len = len(p_array)
      result = []
      for j in range(1, p_len - 2):
         for t in range(points_to_compute):
            p = spline(*p_array[j-1:j+2 + 1], t = t / float(points_to_compute))
            result.append(p)

      return result
