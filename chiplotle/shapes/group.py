from chiplotle.shapes.shape import _Shape

class Group(_Shape):
   '''A group collects together multiple _Shapes, so they
   can be treated as a single object. 
   The elements in a group are stored in order, like a list, so that
   order-specific operation can be performed on groups. 
   i.e., Groups are lists, not sets.
   '''
   def __init__(self, shapes=None):
      _Shape.__init__(self, offset=(0, 0), rotation=0, pivot=(0,0))
      self._shapes = [ ]
      shapes = shapes or [ ]
      self.extend(shapes)


   ## PUBLIC PROPERTIES ##

   @property
   def points(self):
      result = [ ]
      for shape in self:
         result.extend(shape.offset_rotated_points)
      return result


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
      result = self._shapes.pop(indx)
      return result


   ## PRIVATE METHODS ##

   def _check_init_shape(self, shape):
      if not isinstance(shape, _Shape):
         raise TypeError('shape must be an _Shape object.')

   def _check_init_shapes(self, shapes):
      for s in shapes:
         self._check_init_shape(s)


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


if __name__ == '__main__':
   from chiplotle.shapes.group import Group
   from chiplotle.shapes.rectangle import Rectangle
   from chiplotle.tools import io
   import math
   r1 = Rectangle(100, 200, (0, 0))
   r2 = Rectangle(200, 100, (0, 100))
   g1 = Group([r1, r2])
   g1.rotation = math.pi / 3
   g1.offset = (100, 100)
   g2 = Group([g1, Rectangle(50, 400)])
   print g2.format
   io.view(g2)

   