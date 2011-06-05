from chiplotle.hpgl.commands import SI
import py.test

def test_SI_01( ):
   '''SI has default values.'''
   t = SI( )
   
   assert t.format == 'SI;'


def test_SI_02( ):
   t = SI(3, 2)
   
   assert t.format == 'SI3.00,2.00;'


def test_SI_03( ):

   t = SI(3)

   assert py.test.raises(Warning, 't.format')
