from chiplotle import *
from py.test import raises

def test_inflate_hpgl_string_01( ):
   '''An empty string returns an empty list.'''
   t = hpgltools.inflate_hpgl_string('')

   assert t == [ ]
  

def test_inflate_hpgl_string_02( ):
   '''The first argument must be a string.'''
   assert raises(TypeError, 't = hpgltools.inflate_hpgl_string([1,2,3])')


def test_inflate_hpgl_string_03( ):
   '''The function converts a string of HPGL commands into Chiplotle-HPGL instances.'''
   t = hpgltools.inflate_hpgl_string('IN;PU;PA10,10;CI100;')

   assert len(t) == 4
   assert t[0] == IN( )
   assert t[1] == PU( )
   assert t[2] == PA((10, 10))
   assert t[3] == CI(100)


def test_inflate_hpgl_string__filter_01( ):
   '''The function can take a list of HPGL commands to filter out from the result.'''
   t = hpgltools.inflate_hpgl_string('IN;PU;PA10,10;CI100;', ['IN', 'PA'])

   assert len(t) == 2
   assert t[0] == PU( )
   assert t[1] == CI(100)


def test_inflate_hpgl_string__filter_02( ):
   '''The `filter_commands' argument must be a list of two-letter HPGL strings.'''
   e = "t = hpgltools.inflate_hpgl_string('IN;PU;PA10,10;CI100;', 'IN;PU;')"

   assert raises(TypeError, e)
