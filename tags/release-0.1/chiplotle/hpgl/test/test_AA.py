from chiplotle import *
import py.test

def test_AA_01( ):
   t = AA((0,0), 180)

   assert t.angle == 180
   assert t.chordtolerance is None
   assert t.format == 'AA0.0,0.0,180;'


def test_AA_02( ):
   t = AA((0,0), 180, 45)

   assert t.angle == 180
   assert t.chordtolerance == 45
   assert t.format == 'AA0.0,0.0,180,45;'


def test_AA_03( ):
   '''AA must take at least two arguments: position and angle.'''
   assert py.test.raises(TypeError, 'AA((0, 0))')
