from chiplotle.hpgl.commands import FT
from py.test import raises

def test_FT_01( ):
   t = FT( )
   assert t.type is None
   assert t.space is None
   assert t.angle is None
   assert t.format == 'FT;'
   

def test_FT_02( ):
   t = FT(2)
   assert t.type == 2
   assert t.format == 'FT2;'


def test_FT_03( ):
   t = FT(2, .23)
   assert t.type == 2
   assert t.space == 0.23
   assert t.format == 'FT2,0.23;'


def test_FT_04( ):
   t = FT(2, .23, 80.5)
   assert t.type == 2
   assert t.space == 0.23
   assert t.angle == 80.5
   assert t.format == 'FT2,0.23,80.5;'


def test_FT_05( ):
   '''Mandatory parameters missing raises Warning at format time.'''
   t = FT( )
   t.space = .23
   assert t.type is None
   assert t.space == 0.23
   assert t.angle is None
   assert raises(Warning, 't.format')

