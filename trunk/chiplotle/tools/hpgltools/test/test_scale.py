from chiplotle import *
from chiplotle.tools.hpgltools import scale

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
   assert t.xy == [1.5, 3.0]

def test_scale_EA( ):
   '''Scale works on single EA.'''
   t = EA((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]

def test_scale_PU( ):
   '''Scale works on single PU.'''
   t = PU((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]

def test_scale_PD( ):
   '''Scale works on single PD.'''
   t = PD((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]

def test_scale_PA( ):
   '''Scale works on single PA.'''
   t = PA((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]

def test_scale_PR( ):
   '''Scale works on single PR.'''
   t = PR((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]

def test_scale_RA( ):
   '''Scale works on single RA.'''
   t = RA((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]
   
def test_scale_RR( ):
   '''Scale works on single RR.'''
   t = RR((1, 2))
   scale(t, 1.5)
   assert t.xy == [1.5, 3.0]
   

def test_scale_container_01( ):
   t = Container((1, 2), [Circle((10, 10), 100)])
   scale(t, 1.5)
   
   assert t.xy == [1.5, 3]
   assert t[0].xy == [15, 15]
   assert t[0].xyabsolute == [16.5, 18]
   assert t[0].radius == 150
   

def test_scale_hpglcontainer_01( ):
   t = HPGLContainer((1, 2), [PA((1, 2)), PR((2, 3))])
   scale(t, 1.5)

   assert t.xy == [1.5, 3]
   assert t[0].xy == [1.5, 3]
   assert t[1].xy == [3, 4.5]
   assert t.format == 'PA1.50,3.00;PA3.00,6.00;PR3.00,4.50;'
   

def test_scale_list_01( ):
   t = [PA((1, 2)), PU((3, 4))]
   scale(t, 1.5)

   assert t[0].xy == [1.5, 3]
   assert t[1].xy == [4.5, 6]

