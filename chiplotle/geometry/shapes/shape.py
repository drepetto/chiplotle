from chiplotle.geometry.coordinate import Coordinate
from chiplotle.core.interfaces.decoratable import Decoratable

class _Shape(Decoratable):
   '''Abstract class from which all geometric shapes inherit.'''

   language = 'HPGL'

   def __init__(self):
      Decoratable.__init__(self)



   ## OVERRIDES ##
   
   def __repr__(self):
      return self.__class__.__name__ + "( )"
