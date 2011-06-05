from chiplotle.hpgl.commands import SR
import py.test

def test_SR_01( ):
   '''SR can be initialized empty.'''

   t = SR( )
   
   assert t.format == 'SR;'


def test_SR_02( ):

   t = SR(3, 2)
   
   assert t.format == 'SR3.00,2.00;'


def test_SR_03( ):

   t = SR(3)

   assert py.test.raises(Warning, 't.format')
