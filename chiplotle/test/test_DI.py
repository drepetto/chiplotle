from chiplotle import *
from py.test import raises

def test_DI_01( ):
   t = DI( )
   assert t.run == t.rise == None
   assert t.format == 'DI;'


def test_DI_02( ):
   t = DI(23)
   assert t.run == 23
   assert t.rise == None
   assert raises(Warning, 't.format')


def test_DI_03( ):
   t = DI(23, 25.3)
   assert t.run == 23
   assert t.rise == 25.3
   assert t.format == 'DI23,25.3;';

