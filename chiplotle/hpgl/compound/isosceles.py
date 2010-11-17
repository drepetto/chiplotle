from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class Isosceles(_CompoundHPGL):
   '''An isosceles trinagle.'''
   
   _scalable = _CompoundHPGL._scalable + ['height', 'width']

   def __init__(self, xy, width, height, rotation=0, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.height = height
      self.width = width
      self.rotation = rotation
      

   @property
   def _subcommands(self):
      tip = (0, self.height)
      left = (- self.width / 2.0, 0)
      right = (self.width / 2.0 , 0)

      tip = rotate_2d(tip, self.rotation)
      left = rotate_2d(left, self.rotation)
      right = rotate_2d(right, self.rotation)

      
      result = _CompoundHPGL._subcommands.fget(self)
      result += [PU( ), PA(self.xy + tip), PD( ), 
         PA(self.xy + right), PA(self.xy + left), PA(self.xy + tip),
         PU( )]
      return result

   ## OVERRIDES ##
   

