from chiplotle.geometry.coordinate import Coordinate

class _Shape(object):
   '''
      Abstract class from which all geometric shapes inherit.
   
      offset is a Coordinate for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a Coordinate indicating the point around which to rotate
   
   '''

   language = 'HPGL'

   def __init__(self):
      self.offset = Coordinate(0,0)
      self.rotation = 0
      ## pivot point for rotation.
      self.pivot = Coordinate(0,0)

      self.transforms = [ ]

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
