from chiplotle import *
from chiplotle.cfg.get_serial_port import get_serial_port
from serial import Serial

port = get_serial_port( )
if port:
   s = Serial(port=port, baudrate=9600, timeout=0)

   def test_plotter_write_01( ):
      '''write( ) can take a string of raw HPGL commands.'''
      plotter = Plotter(s)
      plotter.write('SP1;PA0,0;PD;PU;')

   def test_plotter_write_02( ):
      '''write( ) can take a Chiplotle HPGL command.'''
      plotter = Plotter(s)
      plotter.write(CI(1000))

   def test_plotter_write_03( ):
      '''write( ) can take list/tuple of raw HPGL commands.'''
      plotter = Plotter(s)
      plotter.write(['SP2;', 'PA0,0;', 'PD;', 'PU;'])

   def test_plotter_write_04( ):
      '''write( ) can take list/tuple of Chiplotle HPGL commands.'''
      plotter = Plotter(s)
      plotter.write([PA((1000, 0)), CI(500)])

