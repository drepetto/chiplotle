from chiplotle import *

def test_label_01( ):

   t = Label((0, 0), 'Hello')

   assert t.xy == [0, 0]
   assert t.text == 'Hello'
   assert t.charsize == (1, 1)
   assert t.direction == None
   assert t.charspace == None
   assert t.linespace == None
   assert t.origin == None
   assert t.slant == None
   assert t.vertical == False
   assert t.format == 'PU;PA0,0;SI1.00,1.00;LBHello\x03;SI;'


def test_label_charsize_01( ):

   t = Label((1, 1), 'Hello')
   t.charsize = (2, 3)

   assert t.charsize == (2, 3)
   assert t.format == 'PU;PA1,1;SI2.00,3.00;LBHello\x03;SI;'


## scale ##

def test_label_scale_01( ):
   t = Label((1, 2), 'Hello', (10, 10))
   hpgltools.scale(t, 1.5)

   assert Label._scalable == ['xy', 'charsize']
   assert t.xy == (1.5, 3)
   assert t.charsize == (15, 15)
