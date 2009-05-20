from chiplotle import *

def test_SI_01( ):
   '''SI has default values.'''
   t = SI( )
   
   assert t.format == 'SI;'


def test_SI_02( ):
   t = SI(3, 2)
   
   assert t.format == 'SI3.0000,2.0000;'

