from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class _Shape(object):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self, offset, rotation, pivot):
      self.offset = CoordinatePair(offset)
      self.rotation = rotation
      ## pivot point for rotation.
      self.pivot = CoordinatePair(pivot)


   ## PUBLIC PROPERTIES ##

   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result


   @property
   def points(self):
      pass


   ## NOTE: rotation and offset implementations should be here, 
   ## in the base class so that one does not have to worry about 
   ## these transformations at all. They come at the end, once
   ## points are generated. 

   @property
   def offset_points(self):
      return [points + self.offset for points in self.points]


   @property
   def offset_rotated_points(self):
      result = [ ]
      for points in self.offset_points:
         ca = rotate_2d(points, self.rotation, self.pivot)
         result.append(ca)
      return result


   ## PRIVATE PROPERTIES ##

   @property
   def _subcommands(self):
      result = [ ]
      if _Shape.language == 'HPGL':
         ## create hpgl commands
         for path in self.offset_rotated_points:
            result += convert_coordinates_to_hpgl_absolute_path(path)
      elif _Shape.language == 'gcode':
         ## create gcode
         print 'Sorry, no g-code support!'
      return result 


   ## OVERRIDES ##
   
   def __repr__(self):
      return self.__class__.__name__ + "( )"
