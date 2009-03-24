from chiplotle import *

def test_AA_01( ):
   t = AA((0,0), 180)
   assert t.angle == 180
   assert t.chordtolerance is None

def test_AA_02( ):
   t = AA((0,0), 180)
   assert t.format == 'AA0.0,0.0,180;'
