from chiplotle.hpgl.compound.compound import _CompoundHPGL

class Container(_CompoundHPGL):
   '''Generic container.'''
   def __init__(self, xy, shapes=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      shapes = shapes or [ ]
      self._check_init_shapes(shapes)
      self._shapes = shapes
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

   def _check_init_shapes(self, shapes):
      for s in shapes:
         if not isinstance(s, _CompoundHPGL):
            raise TypeError('All elements in a container must be _CompoundHPGL objects.')


   ## OVERRIDES ##

   def __delitem__(self, indx):
      del(self._shapes[indx])

   def __getitem__(self, indx):
      return self._shapes[indx]

   def __len__(self):
      return len(self._shapes)

   def __repr__(self):
     return '%s(%d)' % (self._name, len(self))

   def __setitem__(self, i, expr):
      if isinstance(i, int):
         if not isinstance(expr, _CompoundHPGL):
            raise TypeError('Must be _CompoundHPGL')
         self._shapes[i] = expr
      else:
         self._shapes[i.start : i.stop] = expr

   ## ACCESS ##

   def append(self, arg):
      if not isinstance(arg, _CompoundHPGL):
         raise TypeError('Must be _CompoundHPGL.')
      self._shapes.append(arg)

   def extend(self, arg):
      self._check_init_shapes(arg)
      self._shapes.extend(arg)

   def insert(self, i, arg):
      if not isinstance(arg, _CompoundHPGL):
         raise TypeError('Must be _CompoundHPGL.')
      self._shapes.insert(i, arg)

   def remove(self, arg):
      self._shapes.remove(arg)

   def pop(self, indx):
      self._shapes.pop(indx)
