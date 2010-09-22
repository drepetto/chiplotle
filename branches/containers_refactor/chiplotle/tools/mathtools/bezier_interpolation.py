from chiplotle.tools.mathtools.pascal_row import pascal_row
import numpy

def bezier_interpolation(control_points, points_to_compute, weight):
      '''Computes Bezier interpolations from given `control_points`.
      This uses the generalized formula for bezier curves:
      http://en.wikipedia.org/wiki/B%C3%A9zier_curve#Generalization

      - `control_points` : A list of (x, y) control points.
      - `points_to_compute`: An int of the number of points to compute.
      - `weight`: A list of weights for control points.
      '''

      control_points = numpy.array(control_points)
      number_points = len(control_points)
      combinations = pascal_row(number_points-1)
      ts = [t / float(points_to_compute) for t in range(points_to_compute + 1)]

      result = [ ]
      for t in ts:
         tpowers = (t**i for i in range(number_points))
         upowers = reversed([(1-t)**i for i in range(number_points)])
         coefs = numpy.array([c*a*b for c,a,b in zip(combinations,tpowers,upowers)])
         num = numpy.column_stack((coefs*weight*numpy.column_stack(control_points))).sum(axis=0)
         den = (coefs*weight).sum(axis=0)
         if den == 0:
            den = 1
         point = tuple(num/den)
         result.append(point)
      return result
