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

def test_parse_hpgl_string_03( ):
   '''Negative values are handled correnctly.''' 
   s = 'IN;SP2;PU;PA169.33,-0.00;PD;PA169.33,-1.00,170.22,6.32,170.86,12.67;PU;'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['IN', 'SP2', 'PU', 'PA169.33,-0.00', 'PD', 
      'PA169.33,-0.00,170.22,6.32,170.86,12.67', 'PU']

def test_parse_hpgl_string_04( ):
   '''Commands stringed together (with no ; separator) are handled correctly.'''
   s = 'INSP2PUPA2,-1PDRR100PU'
   t = hpgltools.parse_hpgl_string(s)
   assert t == ['IN', 'SP2', 'PU', 'PA2,-1', 'PD', 'RR100', 'PU']


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

