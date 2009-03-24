from chiplotle import *

def test_scalable_01( ):
   '''Empty Scalable defaults to type 'float32'.'''
   t = Scalable([ ])
   assert t.dtype == 'float32'

def test_scalable_02( ):
   '''Scalable initialized with ints has type float32.'''
   t = Scalable([1,2,3,4])
   assert t.dtype == 'float32'

def test_scalable_03( ):
   '''Scalable initialized with floats stays float32.'''
   t = Scalable([1.2,2.3,3,4])
   assert t.dtype == 'float32'



