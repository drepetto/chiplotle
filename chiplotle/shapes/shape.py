from chiplotle.hpgl.coordinate import Coordinate
from chiplotle.tools.hpgltools.convert_coordinates_to_hpgl_absolute_path \
   import convert_coordinates_to_hpgl_absolute_path
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class _Shape(object):
   '''
      Abstract class from which all geometric shapes inherit.
   
      offset is a Coordinate for moving the shape around in 2D space
      rotation is an angle expressed in radians
      pivot is a Coordinate indicating the point around which to rotate
   
   '''

   language = 'HPGL'

   def __init__(self, offset, rotation, pivot):
      self.offset = Coordinate(offset)
      self.rotation = rotation
      ## pivot point for rotation.
      self.pivot = Coordinate(pivot)


   ## PUBLIC PROPERTIES ##

   @property
   def format(self):
      '''Returns the final drawing commands in string format.'''
      result = ''
      for c in self._subcommands:
         result += c.format
      return result


   @property
   def points(self):
      '''Returns a list of CoordinateArrays, each of which represents
      a path (uninterrupted line) in a drawing.'''
      ## must be implemented in concrete sublcasses.
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
