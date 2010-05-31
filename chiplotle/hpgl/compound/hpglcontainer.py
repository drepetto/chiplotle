from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.commands import PA
from chiplotle.tools.hpgltools.is_primitive_absolute import is_primitive_absolute

class HPGLContainer(_CompoundHPGL):
   '''Primitive HPGL commands can be contained in this container.
   The position of primitive absolute HPGL commands (e.g., PA, RA) 
   is relative to the position of this container.'''
   def __init__(self, xy, shapes=None, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self._shapes = [ ]
      shapes = shapes or [ ]
      self.extend(shapes)


   ## PRIVATE METHODS ##

   def _check_init_shape(self, shape):
      if not isinstance(shape, _HPGLPrimitive):
         raise TypeError('All elements must be _HPGLPrimitive objects.')
      if isinstance(shape, _CompoundHPGL):
         raise TypeError('Elements cannot be _CompoundHPGL commands.')

   def _check_init_shapes(self, shapes):
      for s in shapes:
         self._check_init_shape(s)

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PA(self.xyabsolute))
      for s in self:
         if is_primitive_absolute(s):
            result.append(s.__class__(s.xy + self.xyabsolute))
         else:
            result.append(s)
      return result
      result.extend(self)
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


## PUBLIC METHODS ##

   def append(self, arg):
      self._check_init_shape(arg)
      self._shapes.append(arg)

   def extend(self, arg):
      self._check_init_shapes(arg)
      self._shapes.extend(arg)

   def insert(self, i, arg):
      self._check_init_shape(arg)
      self._shapes.insert(i, arg)

   def remove(self, arg):
      self._shapes.remove(arg)

   def pop(self, indx=-1):
      return self._shapes.pop(indx)

