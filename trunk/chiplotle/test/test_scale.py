from chiplotle import *

def test_scale_CI( ):
   '''Scale works on single CI.'''
   t = CI(1, 20)
   scale(t, 1.5)
   assert t.radius == 1.5
   assert t.chordangle == 20 ### chordangle is unmodified
   
def test_scale_ER( ):
   '''Scale works on single ER.'''
   t = ER((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_EA( ):
   '''Scale works on single EA.'''
   t = EA((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_PU( ):
   '''Scale works on single PU.'''
   t = PU((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_PD( ):
   '''Scale works on single PD.'''
   t = PD((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_PA( ):
   '''Scale works on single PA.'''
   t = PA((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_PR( ):
   '''Scale works on single PR.'''
   t = PR((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])

def test_scale_RR( ):
   '''Scale works on single RR.'''
   t = RR((1, 2))
   scale(t, 1.5)
   assert all(t.xy == [1.5, 3.0])
   
