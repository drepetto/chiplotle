from chiplotle.geometry.shapes.circle import circle
from chiplotle.geometry.shapes.cross import cross
from chiplotle.geometry.shapes.rectangle import rectangle
from chiplotle.geometry.transforms.offset import offset
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.label import Label
from chiplotle.geometry.core.coordinate import Coordinate

## TODO should this be a decorator carried around by the shape?

def annotation(shape):
   '''
   Returns informative shape annotations. 
   Good for debugging and general info displaying.

   Annotations:
      max (x, y) coordinate
      min (x, y) coordinate
      width
      height
      center
      centroid

   '''

   annotation = _Annotation(shape)
   return annotation.annotation
   

class _Annotation(object):
   
   def __init__(self, shape, charwidth = 0.05, charheight = 0.1):
      self.shape = shape
      self.charwidth = charwidth
      self.charheight = charheight


   def _annotate_structure(self):
      '''Annotate Group / Path structure?'''
      pass


   def _annotate_properties(self):
      cr = '  center: %s' % self.shape.center
      cd = 'centroid: %s' % self.shape.centroid
      mn, mx = self.shape.minmax_coordinates
      mn = '     min: %s' % mn
      mx = '     max: %s' % mx
      ws = '   width: %.2f' % self.shape.width
      hs = '  height: %.2f' % self.shape.height

      fields = '\n\r'.join([cr, cd, mn, mx, ws, hs, ])
      label = Label(fields, self.charwidth, self.charheight)
      offset(label, self.shape.bottom_left)
      return label

      
   def _annotate_center(self):
      coord = self.shape.center
      label = Label('\n\rcenter: ' + str(coord), 
         self.charwidth, self.charheight, 
         origin = 'top-center')
      c = circle(20)
      cr = cross(50, 50)
      mark = Group([c, cr, label])

      offset(label, coord)
      offset(c, coord)
      offset(cr, coord)

      return mark


   def _annotate_centroid(self):
      coord = self.shape.centroid
      label = Label('\n\rcentroid: ' + str(coord), 
         self.charwidth, self.charheight, 
         origin = 'top-center')
      r = rectangle(20, 20)
      cr = cross(50, 50)
      mark = Group([r, cr, label])

      offset(label, coord)
      offset(r, coord)
      offset(cr, coord)

      return mark


   @property
   def annotation(self):
      result = [ ]
      result.append(self._annotate_center( ))
      result.append(self._annotate_centroid( ))
      result.append(self._annotate_properties( ))
      return Group(result)



## demo
if __name__ == '__main__':
   from chiplotle import *
   from chiplotle.hpgl.formatters import Pen
   from random import randint
   coords = [(randint(0, 4000), randint(0, 4000)) for i in range(20)]
   p = bezier_path(coords, 1)
   r = rectangle(1000, 400)
   offset(r, (-2000, 1000))
   g1 = Group([r, p])
   an = annotation(g1)
   Pen(2)(an)

   g2 = Group([g1, an])
   Pen(1)(g2)

   io.view(g2)
