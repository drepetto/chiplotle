from chiplotle.hpgl.abstract.hpgl import _HPGL


class _HPGLCompound(_HPGL):
   '''Abstract clas for HPGLCompound shapes and decorators.

   Interface (must implement):
      - `_subcommands`
      - `xy` position coordinates.
      - `x` position coordinate.
      - `y` position coordinate.
   '''
   
   ## PUBLIC PROPERTIES ##

   @property
   def xy(self):
      pass

   @property
   def x(self):
      pass
      
   @property
   def y(self):
      pass

   
   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result


   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands(self):
      pass


   ## OVERRIDES ##
   
   def __repr__(self):
      return self.__class__.__name__ + "( )"
