from chiplotle.hpgl.commands import VS

def test_VS_01( ):
   '''Empty initialization.'''
   t = VS( )
   assert t.vel is None
   assert t.pen is None
   assert t.format == 'VS;'


def test_VS_02( ):
   '''Initialize velocity.'''
   t = VS(1)
   assert t.vel == 1
   assert t.pen is None
   assert t.format == 'VS1;'


def test_VS_03( ):
   '''Initialize velocity and pen.'''
   t = VS(1, 2)
   assert t.vel == 1
   assert t.pen == 2
   assert t.format == 'VS1,2;'


def test_VS_03( ):
   '''Setting vel to None formats correctly.'''
   t = VS(1, 2)
   t.vel = None
   assert t.format == 'VS;'
