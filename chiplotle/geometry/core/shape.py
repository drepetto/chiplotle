from chiplotle.geometry.core.hpglformatvisitor import HPGLFormatVisitor
from chiplotle.geometry.core.metadata import MetaData
from chiplotle.geometry.core.shapepropertiesmixin import _ShapePropertiesMixin

class _Shape(_ShapePropertiesMixin):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      self.formatters = set( )
      self.layer = None
      self.meta = MetaData()


   @property
   def format(self):
      if _Shape.language == 'HPGL':
         v = HPGLFormatVisitor()
      else:
         raise ValueError('Sorry, only HPGL supported at the moment.')
      v.visit(self)
      return v.format


   ## overrides ##

   def __repr__(self):
      return str(self)

   def __str__(self):
      name = self.meta.name or ''
      tags = self.meta.tags or ''
      return '%s(%d) %s %s' % (self.__class__.__name__, 
                               len(self), 
                               name, 
                               tags)
