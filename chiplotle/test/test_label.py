from chiplotle import *

def test_label_01( ):
   l = Label(10, 10, 'Hello!')
   assert l.format == 'PU;PA10,10;LBHello!\x03;'

def test_label_02( ):
   '''Line and character spacing format correctly.'''
   l = Label(1, 1, 'hello')
   ### both linespace and charspace must be set for them to format. 
   l.linespace = 2
   l.charspace = 1
   assert l.format == 'PU;PA1,1;ES1.0000,2.0000;LBhello\x03;ES;'

def test_label_03( ):
   '''Vertical text formats correctly.'''
   l = Label(1, 1, 'hello')
   l.vertical = True
   assert l.format == 'PU;PA1,1;DV1;LBhello\x03;DV0;'

def test_label_04( ):
   '''Slant formats correctly.'''
   l = Label(1, 1, 'hello')
   l.slant = 0.5
   assert l.format == 'PU;PA1,1;SL0.5000;LBhello\x03;SL0.0000;'


def test_label_05( ):
   '''Direction formats correctly.'''
   l = Label(1, 1, 'hello')
   l.direction = (1, 2)
   assert l.format == 'PU;PA1,1;DI1.0000,2.0000;LBhello\x03;DI;'

def test_label_06( ):
   '''Origin formats correctly.'''
   l = Label(1, 1, 'hello')
   l.origin = 5
   assert l.format == 'PU;PA1,1;LO5;LBhello\x03;LO1;'

def test_label_07( ):
   '''Pen formats correctly.'''
   l = Label(1, 1, 'hello')
   l.pen = 5
   assert l.format == 'SP5;PU;PA1,1;LBhello\x03;'

def test_label_07( ):
   '''Character size (absolute) formats correctly.'''
   l = Label(1, 1, 'hello')
   l.charsize = (2, 1)
   assert l.format == 'PU;PA1,1;SI2.0000,1.0000;LBhello\x03;SI;'

