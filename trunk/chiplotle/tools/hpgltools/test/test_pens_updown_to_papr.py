from chiplotle import *
from chiplotle.hpgl.commands import *

def test_pens_updown_to_papr_01( ):
   g = [PA([(1, 2)]), PU([(1, 1), (2, 2)])]
   t = hpgltools.pens_updown_to_papr(g)
   assert len(t) == 3
   assert t[0] == PA([(1, 2)])
   assert t[1] == PU( )
   assert t[2] == PA([(1, 1), (2, 2)])


def test_pens_updown_to_papr_02( ):
   g = [PU([(1, 1), (2, 2)])]
   t = hpgltools.pens_updown_to_papr(g)
   assert len(t) == 2
   assert t[0] == PU( )
   assert t[1] == PA([(1, 1), (2, 2)])


def test_pens_updown_to_papr_03( ):
   '''Other HPGL commands are passed untouched.'''
   g = [PA([(0, 0)]), CI(100), PD([(1, 1), (2, 2)]), ER((10, 10))]
   t = hpgltools.pens_updown_to_papr(g)
   assert len(t) == 5
   assert t[0] == PA([(0, 0)])
   assert t[1] == CI(100)
   assert t[2] == PD( )
   assert t[3] == PA([(1, 1), (2, 2)])
   assert t[4] == ER((10, 10))


def test_pens_updown_to_papr_04( ):
   '''The function returns fresh new instances of PA and or PR.'''
   g = [PA(), PD([(1, 1)]), PD([(2, 2)]), PD([(3, 3)])]
   t = hpgltools.pens_updown_to_papr(g)
   assert len(t) == 7
   assert t[2] is not t[4]
   assert t[4] is not t[6]
   
