from chiplotle.hpgl.commands import PA, PD, PU
from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound
from chiplotle.hpgl.compound.group import Group
from chiplotle.hpgl.compound.decorators.hpglcompounddecorator \
   import _HPGLCompoundDecorator

class DConnector(_HPGLCompoundDecorator):
   '''Connects shapes in a Group container with lines.'''

   def __init__(self, hpglcompound, close_connection=True):
      if isinstance(hpglcompound, (list, tuple)):
         hpglcompound = Group((0, 0), hpglcompound) 
      elif not isinstance(hpglcompound, Group):
         raise TypeError('%s must take a list, tuple or Group.' % self._name)
      for shape in hpglcompound:
         if not isinstance(shape, _HPGLCompound):
            raise TypeError('Only Compound HPGL shapes can be connected.')

      _HPGLCompoundDecorator.__init__(self, hpglcompound)
      self.close_connection = close_connection


   @property
   def _subcommands(self):
      result = self.hpglcompound._subcommands
      coords = [ ]
      for shape in self.hpglcompound:
         coords.append(shape.xy)
      ## close connector...
      if self.close_connection:
         coords.append(coords[0])      

      result += [PU( ), PA(coords[0]), PD( ), PA(coords), PU( )]
      return result
