from chiplotle.hpgl.commands import AR
import py.test

def test_AR_01( ):
   t = AR((0,0), 180)

   assert t.angle == 180
   assert t.chordtolerance is None
   assert t.format == 'AR0,0,180.00;'


def test_AR_02( ):
   t = AR((0,0), 180, 45)

   assert t.angle == 180
   assert t.chordtolerance == 45
   assert t.format == 'AR0,0,180.00,45.00;'


def test_AR_03( ):
   '''AR must take at least two arguments: position and angle.'''
   assert py.test.raises(TypeError, 'AR((0, 0))')


def test_AR_format_01( ):
   '''Ints format as ints.'''
   t = AR((0,0), 180)

   assert t.format == 'AR0,0,180.00;'


def test_AR_format_02( ):
   '''Floats format as floats.'''
   t = AR((0,0.0), 180)

   assert t.format == 'AR0.00,0.00,180.00;'
