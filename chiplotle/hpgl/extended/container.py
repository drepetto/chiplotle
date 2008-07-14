from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.scalable import Scalable

class Container(_ExtendedHPGL, list):
   '''Generic container.'''
   def __init__(self, x, y, shapes=None, pen=None):
      _ExtendedHPGL.__init__(self, (x, y), pen)
      list.__init__(self, shapes)
      #self._shapes = shapes or [ ]
      self._linkUp( )

   def _linkUp(self):
      #for s in self._shapes:
      for s in self:
         s._parent = self

   @property
   def _subcommands(self):
      result = _ExtendedHPGL._subcommands.fget(self)
      #for s in self._shapes:
      for s in self:
         result.extend(s._subcommands)
      return result

