from chiplotle import *

def test_get_bounding_box_01( ):
   '''The function can take a list of _HPGLPrimitives.'''
   t = hpgltools.get_bounding_box([PA([(1, 2), (3, 4)])])
   assert t == (CoordinatePair(1, 2), CoordinatePair(3, 4))


def test_get_bounding_box_02( ):
   '''The function can take a list of _HPGLPrimitives.'''
   a = [PA([(1, 2), (3, 4)]), EA((10, -2))]
   t = hpgltools.get_bounding_box(a)
   assert t == (CoordinatePair(1, -2), CoordinatePair(10, 4))


def test_get_bounding_box_03( ):
   '''The function can take a _CompoundHPGL.'''
   a = Rectangle((100, 200), 10, 10)
   t = hpgltools.get_bounding_box(a)
   assert t == ((95, 195), (105, 205))


def test_get_bounding_box_04( ):
   '''The function can take a Group with _HPGLPrimitives.'''
   a = Group((100, 200), [PA((2, 2)), PR((10, 10))])
   t = hpgltools.get_bounding_box(a)
   ## NOTE: should this return a (102, 202) instead of (100, 200)?
   assert t == ((100, 200), (112, 212))
