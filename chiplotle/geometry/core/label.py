from chiplotle.hpgl.label import Label as HPGLLabel
from chiplotle.hpgl.commands import PA
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.shape import _Shape
from chiplotle.tools import mathtools
import math


## TODO should a Label be a path? Probably not.

class Label(_Shape):
   '''
   A text label.
   
   - `text` is the text to be displayed.
   - `charwidth` is the width of characters in cms.
   - `charheight` is the height of characters in cms. 
   - `charspace` is the spacing factor between characters.
   - `linespace` is a spacing factor between lines.
   - `origin` is the origin of the text, can be:
         'top-left'     'top-center'      'top-right'
         'middle-left'  'middle-center'   'middle-right'
         'bottom-left'  'bottom-center'   'bottom-right'
   ''' 

   HPGL_ORIGIN_MAP = {
      'bottom-left'  : 1,
      'middle-left'  : 2,
      'top-left'     : 3,
      'bottom-center': 4,
      'middle-center': 5,
      'top-center'   : 6,
      'bottom-right' : 7,
      'middle-right' : 8,
      'top-right'    : 9}


   def __init__(self, 
      text,
      charwidth, 
      charheight, 
      charspace = None, 
      linespace = None,
      origin = 'bottom-left'):  

      _Shape.__init__(self)

      self.text = text
      self.charspace = charspace
      self.linespace = linespace
      self.origin = origin

      self.points = [(0, 0), (charwidth, 0), (charwidth, charheight)]

      self.never_upside_down = False

   ## PUBLIC PROPERTIES ##

   @property
   def points(self):
      return self._points
   @points.setter
   def points(self, arg):
      self._points = CoordinateArray(arg)


   @property
   def angle(self):
      return self.points.difference[0].angle

   ## TODO make settable...
   @property
   def charwidth(self):
      return self.points.difference[0].magnitude
#   @charwidth.setter
#   def charwidth(self, arg):
#      self._points
      
   @property
   def charheight(self):
      return self.points.difference[1].magnitude

   ## PRIVATE PROPERTIES ##

#   @property
#   def _infix_commands(self):
#      angle = self.angle
#      if self.never_upside_down:
#         if math.pi * 3 / 2.0 > angle > math.pi / 2.0:
#            angle += math.pi
#
#      if _Shape.language == 'HPGL':
#         origin = self.HPGL_ORIGIN_MAP[self.origin]
#         label = HPGLLabel(
#            text = self.text, 
#            charwidth = self.charwidth,
#            charheight = self.charheight,
#            charspace = self.charspace,
#            linespace = self.linespace,
#            origin = origin,
#            direction = mathtools.polar_to_xy((1, angle)),
#            )
#         return [PA(self.points[0]), label]
#
#      elif _Shape.language == 'gcode':
#         print 'Sorry, no g-code support!'
#         raise NotImplementedError


   def __str__(self):
      return '%s(%s)' % (self.__class__.__name__, self.text)

## DEMO CODE

if __name__ == '__main__':
   from chiplotle import *
   
   lb = Label("Hello!", 1, 2, origin = 'bottom-center')
   PenDecorator(Pen(1))(lb) ## we need this for Label to display with hp2xx

   rotate(lb, 3.14 / 4 * 3)
   c = circle(100 / 2.5)
   g = group([c, lb])
   io.view(g)

