from chiplotle.core.interfaces.decoratable import Decoratable
from chiplotle.geometry.core.shapepropertiesmixin import _ShapePropertiesMixin
from chiplotle.geometry.core.metadata import MetaData

class _Shape(Decoratable, _ShapePropertiesMixin):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      Decoratable.__init__(self)
      self.layer = None
      self.meta = MetaData()


   ## overrides ##

   def __repr__(self):
      return str(self)

   def __str__(self):
      name = self.meta.name or ''
      tags = self.meta.tags or ''
      return '%s(%d) "%s" %s' % (self.__class__.__name__, 
                               len(self), 
                               name, 
                               tags)
