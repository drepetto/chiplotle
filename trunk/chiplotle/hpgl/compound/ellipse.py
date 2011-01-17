from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.geometry.vector import Vector
import math

class Ellipse(_HPGLCompoundShape):
   '''
   Compound Ellipse. Can be rotated. Cannot be filled (why not?).
   
   Set width == height for circles.
   
   Rotation is in degrees.
   
   Points returns a list of lists of points, in this case it's just
   one list.
   
   Ellipse code adapted from: http://en.wikipedia.org/wiki/Ellipse
   
   
   ERROR!!! I think this draws the Ellipse at 2 x height and width!
   
   '''

   _scalable = _HPGLCompoundShape._scalable + ['width', 'height']

   def __init__(self, xy, width, height, rotation=0, segments = 36):
      _HPGLCompoundShape.__init__(self, xy) 
      self.width = width
      self.height = height
      self.rotation = rotation
      self.segments = segments

      if rotation != 0:
         print "Sorry, rotation is ignored in this version!"
         rotation = 0

   #I think this should go into all HPGLCompoundShapes!
   @property
   def points(self):
      pi_div_180 = math.pi / 180.0
      
      #(Math.PI/180) converts Degree Value into Radians
      beta = -self.rotation * pi_div_180; 
      
      sin_beta = math.sin(beta);
      cos_beta = math.cos(beta);

      rads_incr = 360.0/float(self.segments)
      
      rads = 0.0
      
      points = []
      
      while rads < 360.0: 
         alpha = rads * pi_div_180
         sin_alpha = math.sin(alpha);
         cos_alpha = math.cos(alpha);
 
         point_x = (self.width * cos_alpha * cos_beta - self.height * sin_alpha * sin_beta);
         point_y = (self.width * cos_alpha * sin_beta + self.height * sin_alpha * cos_beta);
 
         points.append(Vector(point_x, point_y))
         
         rads += rads_incr
    
      #close the ellipse
      rads = 0.0
      alpha = rads * pi_div_180
      sin_alpha = math.sin(alpha);
      cos_alpha = math.cos(alpha);
 
      point_x = (self.width * cos_alpha * cos_beta - self.height * sin_alpha * sin_beta);
      point_y = (self.width * cos_alpha * sin_beta + self.height * sin_alpha * cos_beta);
 
      points.append(Vector(point_x, point_y))
      
      return [points]

      
   @property
   def _subcommands(self):
      
      the_points = self.points[0]
      
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append( PU( ) )
      result.append( PA((self.xy + the_points[0])) )
      result.append( PD() )
      for point in the_points:
         result.append( PA((self.xy + point)) )

      result.append( PU() )

      return result


   