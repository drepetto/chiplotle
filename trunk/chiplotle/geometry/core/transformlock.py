from chiplotle.geometry.core.group import Group
from chiplotle.tools.mathtools.rotate_2d import rotate_coordinate_2d
from chiplotle.tools.geometrytools.scale import scale

class TransformLock(Group):

   def __init__(self, shapes, lock_transforms):
      Group.__init__(self, shapes = shapes)
      self.lock_transforms = set(lock_transforms)
      self.transform_map = {'scale' : self.scale_to_offset,
                            'rotate': self.rotate_to_offset,
                            }

   def get_transform(self, transform):
      fn = transform.func_name
      transform = self.transform_map.get(fn)
      if transform is None:
         raise ValueError("Don't know transform '%s'." % fn)
      return transform

   @staticmethod
   def rotate_to_offset(points, angle, pivot):
      def offset(points, value):
         return points + value
      center = points.center
      new_coord = rotate_coordinate_2d(center, angle, pivot)
      diff = new_coord - center
      return offset, [diff]

   @staticmethod
   def scale_to_offset(points, factor, pivot):
      def offset(points, value):
         return points + value
      #center = get_center(points)
      center = points.center
      new_coord = scale(center, factor, pivot)
      diff = new_coord - center
      return offset, [diff]


## ~~~~~~~~~~~~~~~~~~
if __name__ == '__main__':
   from chiplotle.geometry import shapes
   from chiplotle.geometry import transforms
   from chiplotle import io
   from chiplotle.hpgl import formatters
   import copy
   import math

   def rotation_example():
      r1 = shapes.rectangle(100, 100)
      r2 = shapes.rectangle(200, 200)
      transforms.offset(r2, (400, 0))
      r3 = shapes.rectangle(300, 300)
      transforms.offset(r3, (800, 0))

      tl = TransformLock([r1, r2], ['rotate'])
      start = Group([tl, r3])
      transforms.offset(start, (500, 0))

      mid = copy.deepcopy(start)
      end = copy.deepcopy(start)

      formatters.Pen(3)(start)
      formatters.Pen(2)(mid)
      formatters.Pen(1)(end)
      transforms.rotate(mid, math.pi / 6, (0, 0))
      transforms.rotate(end, math.pi / 3, (0, 0))

      o = shapes.circle(100)
      return Group([start, mid, end, o])


   def scale_example():
      s1 = shapes.star_outline(100, 100, 4)
      transforms.offset(s1, (300, 0))
      transforms.rotate(s1, -math.pi / 4)
      s2 = shapes.star_outline(100, 100, 6)
      transforms.offset(s2, (300, 0))
      transforms.rotate(s2, -math.pi / 2)
      s3 = shapes.star_outline(100, 100, 9)
      transforms.offset(s3, (300, 0))
      transforms.rotate(s3, -math.pi * 3 / 4)

      tl = TransformLock([s1, s2], ['scale'])
      start = Group([tl, s3])

      mid = copy.deepcopy(start)
      end = copy.deepcopy(start)

      formatters.Pen(3)(start)
      formatters.Pen(2)(mid)
      formatters.Pen(1)(end)
      transforms.scale(mid, 2)
      transforms.scale(end, 3)

      o = shapes.circle(100)
      return Group([start, mid, end, o])

   ## go...
   r = rotation_example()
   s = scale_example()

   io.view(Group([s, r]))
