from chiplotle import *
from py.test import raises

def test_convert_coordinates_to_absolute_hpgl_path_01( ):
   '''Vectors can be generic tuples.'''
   c = [(1, 2), (3, 4), (5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA([c[0]])
   assert t[2] == PD( )
   assert t[3] == PA(c[1:])


def test_convert_coordinates_to_absolute_hpgl_path_02( ):
   '''Vectors can be Vectors.'''
   c = [Vector(1, 2), Vector(3, 4), Vector(5, 6)]
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA(c[0].xy)
   assert t[2] == PD( )
   assert t[3] == PA(c[1:])


def test_convert_coordinates_to_absolute_hpgl_path_03( ):
   '''The argument can be a VectorArray'''
   c = VectorArray([Vector(1, 2), Vector(3, 4), Vector(5, 6)])
   t = hpgltools.convert_coordinates_to_hpgl_absolute_path(c)
   assert t[0] == PU( )
   assert t[1] == PA([c[0]])
   assert t[2] == PD( )
   assert t[3] == PA(c[1:])


def test_convert_coordinates_to_absolute_hpgl_path_04( ):
   '''Argument must be a list of coordinate pairs..'''
   c = [1, 2, 3, 4]
   assert raises(errors.InitParameterError, 'hpgltools.convert_coordinates_to_hpgl_absolute_path(c)')


