from chiplotle import *

def test_IP_01( ):
   t = IP( )

   assert t.format == 'IP;'


def test_IP_02( ):
   t = IP((1,2,3,4))

   assert t.format == 'IP1,2,3,4;'
