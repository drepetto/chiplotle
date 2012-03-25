from chiplotle import *
from chiplotle.hpgl.commands import *
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
   assert t[2] == PA([(10, 10)])
   assert t[3] == CI(100)


def test_inflate_hpgl_string_04( ):
   '''HPGL commands need not be separated by ;.'''
   s = 'INPA10,10PDCI100'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 4
   assert t[0] == IN( )
   assert t[1] == PA([(10, 10)])
   assert t[2] == PD( )
   assert t[3] == CI(100)


## AR AA ##

def test_inflate_hpgl_string_05( ):
   '''AA and AR are with only coordinates and angle are imported correctly.'''
   s = 'IN;AA10,10,90;'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 2
   assert t[0] == IN( )
   assert t[1] == AA((10, 10), 90)


def test_inflate_hpgl_string_06( ):
   '''AA and AR are with all parameters are imported correctly.'''
   s = 'IN;AA10,10,90,10.2;'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 2
   assert t[0] == IN( )
   assert t[1] == AA((10, 10), 90, 10.2)


## two point commands ##

def test_inflate_hpgl_string_IW():
   '''IW.'''
   s = 'IW1,2,3,4;'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 1
   assert t[0] == IW([(1, 2), (3, 4)])

def test_inflate_hpgl_string_SC():
   '''SC.'''
   s = 'SC1,2,3,4;'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 1
   assert t[0] == SC([(1, 2), (3, 4)])

def test_inflate_hpgl_string_IP():
   '''IP.'''
   s = 'IP1,2,3,4;'
   t = hpgltools.inflate_hpgl_string(s)
   assert len(t) == 1
   assert t[0] == IP([(1, 2), (3, 4)])

## FILTERING ##

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
