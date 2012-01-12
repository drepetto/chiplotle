from chiplotle import *
from chiplotle.hpgl.commands import *

def test_pr_to_pa_01( ):
   '''PR with one coordinate works.'''
   pr = PR([(1, 2)])
   t = hpgltools.pr_to_pa(pr, (0, 0))
   assert isinstance(t, PA) 
   assert t.xy == CoordinateArray([(1, 2)])
   

def test_pr_to_pa_02( ):
   '''PR with more than one coordinate works.'''
   pr = PR([(1, 2), (1, 1), (-2, 1)])
   t = hpgltools.pr_to_pa(pr)
   assert isinstance(t, PA) 
   assert t.xy == CoordinateArray([(1, 2), (2, 3), (0, 4)])
   

def test_pr_to_pa_03( ):
   '''PR with mpty coordinate array results in empty PA.'''
   pr = PR( )
   t = hpgltools.pr_to_pa(pr)
   assert isinstance(t, PA) 
   assert t.xy == CoordinateArray([ ])


def test_pr_to_pa_04( ):
   '''The function takes the optional argument `starting_position`.'''
   pr = PR([(1, 1), (1, 1)])
   t = hpgltools.pr_to_pa(pr, (10, 20))
   assert isinstance(t, PA) 
   assert t.xy == CoordinateArray([(11, 21), (12, 22)])
