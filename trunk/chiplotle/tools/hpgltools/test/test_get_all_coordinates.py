from chiplotle import *

def test_get_all_coordinates_01( ):
   '''get_all_coordinates( ) works with _HPGLPrimitives.'''
   t = [PA((1, 2)), PR((1, 1)), ER((1, 1)), CI(100)]
   c = hpgltools.get_all_coordinates(t)
   assert len(c) == 3
   assert c[0] == Vector(1, 2)
   assert c[1] == Vector(2, 3)
   assert c[2] == Vector(3, 4)
 

def test_get_all_coordinates_02( ):
   '''get_all_coordinates( ) works with _HPGLCompound.'''
   t =  [Rectangle((5, 5), 10, 10)]
   c = hpgltools.get_all_coordinates(t)
   assert len(c) == 6
   assert c[0] == Vector(5, 5)
   assert c[1] == Vector(0, 10)
   assert c[2] == Vector(10, 10)
   assert c[3] == Vector(10, 0)
   assert c[4] == Vector(0, 0)
   assert c[5] == Vector(0, 10)
 
