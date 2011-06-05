from chiplotle.hpgl.commands import SetHandshakeMode
from py.test import raises

def test_dci_sethandshakemode_01( ):
   '''SetHandshakeMode can take no parameters.'''
   t = SetHandshakeMode( )

   assert t.format == '\x1b.P'


def test_dci_sethandshakemode_02( ):
   '''SetHandshakeMode can take None, 0, 1, 2 or 3 to set the mode.'''
   t = SetHandshakeMode(1)

   assert t.format == '\x1b.P1'


def test_dci_sethandshakemode_03( ):
   '''SetHandshakeMode cannot take a value other than None, 0, 1, 2 or 3.'''
   assert raises(ValueError, 't = SetHandshakeMode(32)')


