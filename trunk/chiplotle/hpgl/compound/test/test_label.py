from chiplotle import *

def test_label_01( ):

   t = Label((0, 0), 'Hello')

   assert t.xy.tolist( ) == [0, 0]
   assert t.text == 'Hello'
   assert t.charsize == None
   assert t.charsize == None
   assert t.direction == None
   assert t.charspace == None
   assert t.linespace == None
   assert t.origin == None
   assert t.slant == None
   assert t.vertical == False
   assert t.format == 'PU;PA0.00,0.00;LBHello\x03;'


def test_label_charsize_01( ):

   t = Label((1, 1), 'Hello')
   t.charsize = (2, 3)

   assert isinstance(t.charsize, Scalable)
   assert t.charsize.tolist( ) == [2, 3]
   assert t.format == 'PU;PA1.00,1.00;SI2.00,3.00;LBHello\x03;SI;'
