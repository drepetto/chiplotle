from chiplotle import *
from chiplotle.utils.instantiate_plotter import instantiate_plotter

plotter = instantiate_plotter(wait_time = 3)
if plotter:

   def test_plotter_write_01( ):
      '''write( ) can take a string of raw HPGL commands.'''

      plotter.write('SP1;PA0,0;PD;PU;')


   def test_plotter_write_02( ):
      '''write( ) can take a Chiplotle HPGL command.'''

      plotter.write(CI(1000))


   def test_plotter_write_03( ):
      '''write( ) can take list/tuple of raw HPGL commands.'''

      plotter.write(['SP2;', 'PA0,0;', 'PD;', 'PU;'])


   def test_plotter_write_04( ):
      '''write( ) can take list/tuple of Chiplotle HPGL commands.'''

      plotter.write([PA((1000, 0)), CI(500)])

