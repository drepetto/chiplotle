from chiplotle.hpgl.commands import DI
from py.test import raises

def test_DI_01( ):
   t = DI( )

   assert t.run == t.rise == None
   assert t.format == 'DI;'


def test_DI_02( ):
   '''both run and rise (or none) must be set for formatting.'''

   t = DI(23)

   assert t.run == 23
   assert t.rise == None
   assert raises(Warning, 't.format')


def test_DI_03( ):
   '''run can be 0.'''

   t = DI(0, 25.3)

   assert t.run == 0
   assert t.rise == 25.3
   assert t.format == 'DI0.00,25.30;';

