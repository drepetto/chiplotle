from chiplotle.geometry.core.path import Path
from chiplotle.geometry.transforms.offset import offset

def arrange_shapes_on_path(shapes, path):

   if not isinstance(path, Path):
      raise TypeError
   if len(shapes) != len(path):
      raise ValueError('len(shapes) == len(path) must be true.')

   for shape, coord in zip(shapes, path.points):
      offset(shape, coord)



if __name__ == '__main__':
   from chiplotle import *
   import random

   count = 10
   coords = [random.randint(0, 4000) for i in range(count * 2)]
   circs = [circle(100) for i in range(count)]
   p = Path(coords)
   PenDecorator(Pen(2))(p)

   arrange_shapes_on_path(circs, p)

   io.view(group(circs + [p]))
