from chiplotle import *
from chiplotle.utils.plottertools import instantiate_plotters


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


plotter = instantiate_plotters( )[0]

test_plotter_write_01( )
test_plotter_write_02( )
test_plotter_write_03( )
test_plotter_write_04( )
