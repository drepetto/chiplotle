from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.transforms.offset import Offset

def test_nondestructive_offset_01( ):
   '''Non-destructive Offset works on a Group with Paths.'''
   p = Path([(1, 2), (3, 4)])
   t = Group([p])
   o = Offset(1, 2)
   o(t)
   ## points are unmodified...
   assert t[0].points == CoordinateArray([(1, 2), (3, 4)])
   assert t.transforms[0] == o
   assert len(t.transforms) == 1
   assert t._subcommands[0]._transformed_points == CoordinateArray([(2, 4), (4, 6)])
