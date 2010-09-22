from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.compound.newcompound import _NewCompoundHPGL
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.tools.hpgltools import is_primitive_absolute 
import copy

class Group(_NewCompoundHPGL):
   '''A group collects together multiple Chiplotle HPGL commands, so they
   can be treated as a single object. 
   Group has a position (xy) attribute. 
   '''
   def __init__(self, xy, shapes=None, pen=None):
      _NewCompoundHPGL.__init__(self, xy, pen)
      self._shapes = [ ]
      shapes = shapes or [ ]
      self.extend(shapes)


   ## PRIVATE METHODS ##

   def _check_init_shape(self, shape):
      if not isinstance(shape, _HPGL):
         raise TypeError('shape must be an _HPGL object.')

   def _check_init_shapes(self, shapes):
      for s in shapes:
         self._check_init_shape(s)

   @property
   def _subcommands(self):
      result = _NewCompoundHPGL._subcommands.fget(self)
      for s in self:
         if isinstance(s, _HPGLPrimitive):
            if is_primitive_absolute(s):
               s = copy.copy(s)
               s.xy += self.xy
            result.append(s)
         ## TODO: remove `isinstance(s, _CompoundHPGL)` once these are deprecated.
         elif isinstance(s, _NewCompoundHPGL) or isinstance(s, _CompoundHPGL):
            s = copy.copy(s)
            s.xy += self.xy
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
      arg.parentage._cut( )

   def pop(self, indx=-1):
      result = self._shapes[indx]
      result.parentage._cut( )
      return result
