from numpy import array

def catmull_interpolation(control_points, points_to_compute):
      '''Computes Catmull-Rom interpolations from given `control_points`.
      first and last point are not on the curve, but define
      initial and final tangent
      - `control_points` : A list of (x, y) control points.
      - `points_to_compute`: An int of the number of points to compute.
      '''
      p_array = array(control_points)
      p_len = len(p_array)

      def spline_4p(t, p_1, p0, p1, p2 ):
         point = (t*((2-t)*t - 1) * p_1
        + (t*t*(3*t - 5) + 2) * p0
        + t*((4 - 3*t)*t + 1) * p1
        + (t-1)*t*t         * p2 ) / 2

         return point


      result = []
      for j in range(1, p_len-2):
         for t in range(points_to_compute):
            p = spline_4p(t/float(points_to_compute), p_array[j-1],
            p_array[j], p_array[j+1], p_array[j+2])
            result.append(p)

      return result
