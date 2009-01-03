from chiplotle import *
from serial import Serial

s = Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=0)

def test_plotter_write_01( ):
   '''write( ) can take a string of raw HPGL commands.'''
   plotter = Plotter(s)
   plotter.write('PD;')

def test_plotter_write_02( ):
   '''write( ) can take a Chiplotle HPGL command.'''
   plotter = Plotter(s)
   plotter.write(PD( ))

def test_plotter_write_03( ):
   '''write( ) can take list/tuple of raw HPGL commands.'''
   plotter = Plotter(s)
   plotter.write(['PD;', 'PD;', 'PA0,0;'])

def test_plotter_write_04( ):
   '''write( ) can take list/tuple of Chiplotle HPGL commands.'''
   plotter = Plotter(s)
   plotter.write([PD( ), PU( )])

