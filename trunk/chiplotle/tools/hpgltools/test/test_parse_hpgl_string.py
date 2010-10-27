from chiplotle import *

def test_parse_hpgl_string_01( ):
   '''Coma separated integer arguments numbers are handled properly.'''
   s = 'IN;PA0,0PD1,2;PU3,4PD'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['IN', 'PA0,0', 'PD1,2', 'PU3,4', 'PD']


def test_parse_hpgl_string_02( ):
   '''Coma separated floating point numbers are handled correctly.'''
   s = 'IN;PA0,0.1PD1.33,2.0;PU3,4PD'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['IN', 'PA0,0.1', 'PD1.33,2.0', 'PU3,4', 'PD']


## DCI (escape) commands ##

def test_parse_hpgl_string_03( ):
   '''Plotter On DCI is captured.'''
   s = '\x1b.YIN;PA0,0;'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['\x1b.Y', 'IN', 'PA0,0']


def test_parse_hpgl_string_03b( ):
   '''Plotter On DCI is captured.'''
   s = '\x1b.(IN;PA0,0;'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['\x1b.(', 'IN', 'PA0,0']

