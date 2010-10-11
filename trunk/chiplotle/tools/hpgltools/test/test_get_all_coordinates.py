from chiplotle import *

def test_get_all_coordinates_01( ):
   '''get_all_coordinates( ) works with _HPGLPrimitives.'''
   t = [PA((1, 2)), PR((1, 1)), ER((1, 1)), CI(100)]
   c = hpgltools.get_all_coordinates(t)
   assert len(c) == 3
   assert c[0] == (1, 2)
   assert c[1] == (2, 3)
   assert c[2] == (3, 4)
 

def test_get_all_coordinates_02( ):
   '''get_all_coordinates( ) works with _CompoundHPGL.'''
   t =  [Rectangle((5, 5), 10, 10)]
   c = hpgltools.get_all_coordinates(t)
   assert len(c) == 6
   assert c[0] == (5, 5)
   assert c[1] == (0, 10)
   assert c[2] == (10, 10)
   assert c[3] == (10, 0)
   assert c[4] == (0, 0)
   assert c[5] == (0, 10)
 


