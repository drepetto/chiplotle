from chiplotle.hpgl.compound.compound import _CompoundHPGL

class Container(_CompoundHPGL, list):
   '''Generic container.'''
   def __init__(self, xy, shapes=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      shapes = shapes or [ ]
      list.__init__(self, shapes)
      self._linkUp( )

   def _linkUp(self):
      for s in self:
         s._parent = self

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      for s in self:
         result.extend(s._subcommands)
      return result

   def __repr__(self):
     return '%s(%d)' % (self._name, len(self))
