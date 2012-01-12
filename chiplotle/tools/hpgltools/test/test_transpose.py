from chiplotle import *
from chiplotle.hpgl.commands import *
from chiplotle.tools.hpgltools import transpose

def test_transpose_CI( ):
   '''Transpose correctly ignores CI attributes.'''
   t = CI(1, 20)
   transpose(t, (1.5, -2.5))
   assert t.radius == 1
   assert t.chordangle == 20 

def test_transpose_EA( ):
   '''Transpose works on single EA.'''
   t = EA((1, 2))
   transpose(t, (1.5, -2.5))
   assert t.xy == Coordinate(2.5, -0.5)

def test_transpose_ER( ):
   '''Transpose correctly ignores relative positions in ER.'''
   t = ER((1, 2))
   transpose(t, (1.5, -2.5))
   assert t.xy == Coordinate(1, 2)

def test_transpose_PU( ):
   '''Transpose ignores PU because behavior of PU depends on previous 
   PA or PR.'''
   t = PU([(1, 2)])
   transpose(t, (1.5, -2.5))
   assert t.xy == CoordinateArray([(1, 2)])

def test_transpose_PD( ):
   '''Transpose ignores PD.'''
   t = PD([(1, 2)])
   transpose(t, (1.5, -2.5))
   assert t.xy == CoordinateArray([(1, 2)])

def test_transpose_PA( ):
   '''Transpose works on a single PA.'''
   t = PA([(1, 2)])
   transpose(t, (1.5, -2.5))
   assert t.xy == CoordinateArray([(2.5, -0.5)])

def test_transpose_PR( ):
   '''Transpose correctly ignores relative positions in PR.'''
   t = PR([(1, 2)])
   transpose(t, (1.5, -2.5))
   assert t.xy == CoordinateArray([(1, 2)])

def test_transpose_RA( ):
   '''Transpose works on single RA.'''
   t = RA((1, 2))
   transpose(t, (1.5, -2.5))
   assert t.xy == Coordinate(2.5, -0.5)

def test_transpose_RR( ):
   '''Transpose correctly ignores relative positions in RR.'''
   t = RR((1, 2))
   transpose(t, (1.5, -2.5))
   assert t.xy == Coordinate(1, 2)
