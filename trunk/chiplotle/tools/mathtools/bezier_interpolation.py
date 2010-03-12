from chiplotle.tools.mathtools.pascal_row import pascal_row

def bezier_interpolation(control_points, points_to_compute):
      '''Computes Bezier interpolations from given `control_points`.
      This uses the generalized formula for bezier curves:
      http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization

      - `control_points` : A list of (x, y) control points.
      - `points_to_compute`: An int of the number of points to compute.
      '''

      number_points = len(control_points)
      combinations = pascal_row(number_points-1)
      ts = [t / float(points_to_compute) for t in range(points_to_compute + 1)]

      result = [ ]
      for t in ts:
         tpowers = (t**i for i in range(number_points))
         upowers = reversed([(1-t)**i for i in range(number_points)])
         coefs = [c*a*b for c,a,b in zip(combinations,tpowers,upowers)]
         point = tuple(sum([coef*p for coef,p in zip(coefs,ps)]) \
            for ps in zip(*control_points))
         result.append(point)
      return result
