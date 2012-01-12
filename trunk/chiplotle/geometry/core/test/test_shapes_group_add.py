from chiplotle import *
from chiplotle.geometry.core.group import Group
from chiplotle.geometry.core.path import Path
from py.test import raises 

'''A Group is offset with the + operator.'''

'''A Group with paths works as expected.'''

def test_shapes_group_add_01( ):
   '''Group + int is not allowed.'''
   a = Group([Path([(1, 2), (3, 4)]), Path([(5, 6), (7, 8)])])
   assert raises(TypeError, 't = a + 2')


def test_shapes_group_add_02( ):
   '''int + Group is not allowed.'''
   a = Group([Path([(1, 2), (3, 4)]), Path([(5, 6), (7, 8)])])
   assert raises(TypeError, 't = 2 + a')
