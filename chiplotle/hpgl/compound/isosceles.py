from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class Isosceles(_HPGLCompoundShape):
   '''An isosceles trinagle.'''
   
   _scalable = _HPGLCompoundShape._scalable + ['height', 'width']

   def __init__(self, xy, width, height, rotation=0):
      _HPGLCompoundShape.__init__(self, xy)
      self.height = height
      self.width = width
      self.rotation = rotation
      
      if rotation != 0:
         print "Sorry, rotation is ignored in this version!"
         rotation = 0

   @property
   def points(self):
      tip = (0, self.height)
      left = (- self.width / 2.0, 0)
      right = (self.width / 2.0, 0)
      
      return [[tip, left, right]]

   @property
   def _subcommands(self):

      the_points = self.points[0]
      tip = the_points[0]
      left = the_points[1]
      right = the_points[2]

      
      result = _HPGLCompoundShape._subcommands.fget(self)
      result += [PU( ), PA(self.xy + tip), PD( ), 
         PA(self.xy + right), PA(self.xy + left), PA(self.xy + tip),
         PU( )]
      return result

