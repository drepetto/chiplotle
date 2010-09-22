from math import sin, cos, pow


def superformula(a, b, m, n1, n2, n3, phi):
   ''' Computes the position of the point on a
   superformula curve.
   Superformula has first been proposed by Johan Gielis
   and is a generalization of superellipse.
   see: http://en.wikipedia.org/wiki/Superformula
   '''

   t1 = cos(m * phi / 4.0) / a
   t1 = abs(t1)
   t1 = pow(t1, n2)

   t2 = sin(m * phi / 4.0) / b
   t2 = abs(t2)
   t2 = pow(t2, n3)

   t3 = -1 / float(n1)
   r = pow(t1 + t2, t3)
   if abs(r) == 0:
      return (0,0)
   else:
      return (r * cos(phi), r * sin(phi))
