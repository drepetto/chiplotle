from chiplotle import *

def test_scalable_01( ):
   '''Scalable defaults to type 'float32'.'''
   t = Scalable([ ])
   assert t.dtype == 'float32'


