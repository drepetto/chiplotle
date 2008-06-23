from chiplotle import *

def test_label_01( ):
   l = Label(10, 10, 'Hello!')
   assert l.str == 'PU10,10;LBHello!\x03;'

