from chiplotle.core.interfaces.decoratable import Decoratable
from chiplotle.geometry.core.shapepropertiesmixin import _ShapePropertiesMixin

class _Shape(Decoratable, _ShapePropertiesMixin):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      Decoratable.__init__(self)
      self.layer = None


   ## overrides ##

   def __repr__(self):
      return str(self)

   def __str__(self):
      return '%s(%d)' % (self.__class__.__name__, len(self))
