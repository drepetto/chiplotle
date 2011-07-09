from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.transformlock import TransformLock
from chiplotle.geometry import shapes
from chiplotle.geometry import transforms
import copy
import math
import py.test

## test construction ##

def test_transformlock_01():
   '''A TransformLock can be empty.'''
   t = TransformLock([], [])
   assert len(t) == 0

def test_transformlock_02():
   '''A TransformLock can have no tranformations to lock.'''
   r = shapes.rectangle(100, 100)
   t = TransformLock([r], [])
   assert t.lock_transforms == set()
   assert t._shapes == [r]
   
def test_transformlock_03():
   '''A TransformLock takes exactly two arguments.'''
   expr = 't = TransformLock([shapes.rectangle(100, 100)])'
   assert py.test.raises(TypeError, expr)


## test transforms ##

def test_transformlock_transforms_rotate_01():
   '''Shapes under a TransformLock are not rotated under a rotate transform; 
   they are just offset to the rotation point.'''
   t = rotation_locked_rectangle_pair()
   transforms.offset(t, (200, 0))
   assert_rotation_preserves_diff(t)
   assert_rotation_changes_coords(t)

def test_transformlock_transforms_rotate_02():
   '''Locks work within groups.'''
   t = rotation_locked_rectangle_pair()
   g = Group([Group([t])])
   transforms.offset(g, (200, 0))
   assert_rotation_preserves_diff(g)
   assert_rotation_changes_coords(g)

def test_transformlock_transforms_rotate_03():
   '''Scaling affects rotation-locked shapes.'''
   t = rotation_locked_rectangle_pair()
   transforms.offset(t, (200, 0))
   assert_scaling_affects_rotation_locked_shapes(t)

def test_transformlock_transforms_scale_01():
   '''Shapes under a TrsnformLock are not scaled under a scale transform
   they are just offset to the scale point.'''
   t = scale_locked_rectangle_pair()
   transforms.offset(t, (200, 0))
   assert_scaling_preserves_diff(t)
   assert_scaling_changes_coords(t)
   
def test_transformlock_transforms_scale_02():
   '''Locks work within groups.'''
   t = scale_locked_rectangle_pair()
   g = Group([Group([t])])
   transforms.scale(g, 2)
   assert_scaling_preserves_diff(g)
   assert_scaling_changes_coords(g)


## helpers ##

def rotation_locked_rectangle_pair():
   return _transformlock_rectangle_pair(['rotate'])

def scale_locked_rectangle_pair():
   return _transformlock_rectangle_pair(['scale'])


def assert_scaling_preserves_diff(shape):
   _assert_transform_preserves_diff(shape, transforms.scale, [2])

def assert_rotation_preserves_diff(shape):
   _assert_transform_preserves_diff(shape, transforms.rotate, [math.pi / 2])

def assert_rotation_changes_coords(shape):
   _assert_transform_changes_coords(shape, transforms.rotate, [math.pi / 2])

def assert_scaling_changes_coords(shape):
   _assert_transform_changes_coords(shape, transforms.scale, [2])

def assert_scaling_affects_rotation_locked_shapes(shape):
   points_before  = CoordinateArray(shape.points).difference
   minmax_before  = shape.minmax_coordinates
   transforms.scale(shape, 2)
   points_after   = CoordinateArray(shape.points).difference
   minmax_after   = shape.minmax_coordinates
   assert points_before != points_after
   assert CoordinateArray(minmax_before) * 2 == CoordinateArray(minmax_after)


## private ##

def _assert_transform_preserves_diff(shape, transform, trans_args):
   points_before = CoordinateArray(shape.points).difference
   transform(shape, *trans_args)
   points_after = CoordinateArray(shape.points).difference
   assert points_before == points_after

def _assert_transform_changes_coords(shape, transform, trans_args):
   points_before = CoordinateArray(shape.points)
   transform(shape, *trans_args)
   points_after = CoordinateArray(shape.points)
   assert points_before != points_after

def _transformlock_rectangle_pair(trans_locks):
   r1 = shapes.rectangle(100, 100)
   r2 = copy.deepcopy(r1)
   transforms.offset(r2, (200, 0))
   return TransformLock([r1, r2], trans_locks)

