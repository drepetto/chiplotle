from chiplotle.geometry.coordinate import Coordinate

class _Shape(object):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      pass
      #self.transforms = [ ]


   ## PUBLIC PROPERTIES ##

   @property
   def format(self):
      '''Returns the final drawing commands in string format.'''
      result = ''
      for c in self._subcommands:
         result += c.format
      return result


   @property
   def _subcommands(self):
      raise NotImplementedError


   ## OVERRIDES ##
   
   def __repr__(self):
      return self.__class__.__name__ + "( )"
