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
      

   @property
   def _subcommands(self):
      tip = (self.height, 0)
      left = (0, - self.width / 2.0)
      right = (0, self.width / 2.0)

      tip = rotate_2d(tip, self.rotation)
      left = rotate_2d(left, self.rotation)
      right = rotate_2d(right, self.rotation)

      
      result = _HPGLCompoundShape._subcommands.fget(self)
      result += [PU( ), PA(self.xy + tip), PD( ), 
         PA(self.xy + right), PA(self.xy + left), PA(self.xy + tip),
         PU( )]
      return result

   ## OVERRIDES ##
   

