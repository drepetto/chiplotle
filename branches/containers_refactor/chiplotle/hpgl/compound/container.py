from chiplotle.hpgl.compound.compound import _CompoundHPGL

class Container(_CompoundHPGL):
   '''Generic container for CompoundHPGL commands. 
   Only _CompoundHPGL commands can be contained by this Container.'''
   def __init__(self, xy, shapes=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self._shapes = [ ]
      shapes = shapes or [ ]
      self.extend(shapes)


   ## PRIVATE METHODS ##

   def _check_init_shape(self, shape):
      if not isinstance(shape, _CompoundHPGL):
         raise TypeError('shape must be an _CompoundHPGL object.')

   def _check_init_shapes(self, shapes):
      for s in shapes:
         if not isinstance(s, _CompoundHPGL):
            raise TypeError('All elements must be _CompoundHPGL objects.')

   ## TODO: move this to ParentageInterface?
   def _link_subshapes_to_self(self, arg):
      if not isinstance(arg, (list, tuple)):
         arg = [arg]
      for s in arg:
         s.parentage._switch(self)

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      for s in self:
         result.extend(s._subcommands)
      return result


   ## OVERRIDES ##

   def __delitem__(self, indx):
      del(self._shapes[indx])

   def __getitem__(self, indx):
      return self._shapes[indx]

   def __len__(self):
      return len(self._shapes)

   def __repr__(self):
     return '%s(%d)' % (self._name, len(self))

   def __setitem__(self, i, arg):
      if isinstance(i, int):
         self._check_init_shape(arg)
         self._shapes[i] = arg
      else:
         self._check_init_shapes(arg)
         self._shapes[i.start : i.stop] = arg
      self._link_subshapes_to_self(arg)


## PUBLIC METHODS ##

   def append(self, arg):
      self._check_init_shape(arg)
      self._link_subshapes_to_self(arg)
      self._shapes.append(arg)

   def extend(self, arg):
      self._check_init_shapes(arg)
      self._link_subshapes_to_self(arg)
      self._shapes.extend(arg)

   def insert(self, i, arg):
      self._check_init_shape(arg)
      self._link_subshapes_to_self(arg)
      self._shapes.insert(i, arg)

   def remove(self, arg):
      arg.parentage._cut( )

   def pop(self, indx=-1):
      result = self._shapes[indx]
      result.parentage._cut( )
      return result
