from chiplotle import *
from chiplotle.geometry.shapes.group import Group
from chiplotle.geometry.shapes.path import Path
import py.test

'''A Group is offset with the + operator.'''

'''A Group with paths works as expected.'''

def test_shapes_group_add_01( ):
   '''Group + int returns a new Group.'''
   a = Group([Path([(1, 2), (3, 4)]), Path([(5, 6), (7, 8)])])
   t = a + 2
   assert isinstance(t, Group)
   assert isinstance(t[0], Path)
   assert isinstance(t[1], Path)
   assert t[0].points == CoordinateArray([(3, 4), (5, 6)])
   assert t[1].points == CoordinateArray([(7, 8), (9, 10)])


def test_shapes_group_add_02( ):
   '''int + Group returns a new Group.'''
   a = Group([Path([(1, 2), (3, 4)]), Path([(5, 6), (7, 8)])])
   t = 2 + a
   assert isinstance(t, Group)
   assert isinstance(t[0], Path)
   assert isinstance(t[1], Path)
   assert t[0].points == CoordinateArray([(3, 4), (5, 6)])
   assert t[1].points == CoordinateArray([(7, 8), (9, 10)])


'''A Group with Groups works as expected.'''

def test_shapes_group_add_03( ):
   '''Group + int returns a new Group.'''
   b = Group([Path([(1, 2), (3, 4)])])
   a = Group([b, Path([(5, 6), (7, 8)])])
   t = a + 2
   assert len(t) == 2
   assert isinstance(t, Group)
   assert isinstance(t[0], Group)
   assert isinstance(t[1], Path)
   assert isinstance(t[0][0], Path)
   assert t[0][0].points == CoordinateArray([(3, 4), (5, 6)])
   assert t[1].points == CoordinateArray([(7, 8), (9, 10)])


def test_shapes_group_add_04( ):
   '''int + Group returns a new Group.'''
   b = Group([Path([(1, 2), (3, 4)])])
   a = Group([b, Path([(5, 6), (7, 8)])])
   t = 2 + a
   assert len(t) == 2
   assert isinstance(t, Group)
   assert isinstance(t[0], Group)
   assert isinstance(t[1], Path)
   assert isinstance(t[0][0], Path)
   assert t[0][0].points == CoordinateArray([(3, 4), (5, 6)])
   assert t[1].points == CoordinateArray([(7, 8), (9, 10)])


