from chiplotle import *

def test_label_01( ):
   l = Label(10, 10, 'Hello!')
   assert l.format == 'PU;PA10,10;LBHello!\x03;'

