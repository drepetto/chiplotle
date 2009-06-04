from chiplotle import *
import py.test

def test_SI_01( ):
   '''SI has default values.'''
   t = SI( )
   
   assert t.format == 'SI;'


def test_SI_02( ):
   t = SI(3, 2)
   
   assert t.format == 'SI3.00,2.00;'


def test_SR_03( ):

   t = SR(3)

   assert py.test.raises(Warning, 't.format')
