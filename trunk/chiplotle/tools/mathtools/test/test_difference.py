from chiplotle import *

def test_difference_01( ):
   '''Computes the difference of a list of ints.'''
   a = [1, 2, 3, 4]
   t = mathtools.difference(a)
   assert t == [1, 1, 1]
   assert isinstance(t, list)


def test_difference_02( ):
   '''Computes the difference of a CoordinateArray.'''
   a = CoordinateArray([(1, 2), (3, 4), (4, 4)])
   t = mathtools.difference(a)
   assert t == CoordinateArray([(2, 2), (1, 0)])
   assert isinstance(t, CoordinateArray)


def test_difference_03( ):
   '''The argument can be empty.'''
   t = mathtools.difference([ ])
   assert t == [ ]
   assert isinstance(t, list)


def test_difference_04( ):
   '''The argument can have one element.'''
   t = mathtools.difference([2])
   assert t == [ ]
   assert isinstance(t, list)
