from chiplotle import *
from chiplotle.hpgl.commands import *
from chiplotle.tools.plottertools.instantiate_virtual_plotter \
   import instantiate_virtual_plotter


def test_plotter_write_01( ):
   '''write( ) can take a string of raw HPGL commands.'''
   p = instantiate_virtual_plotter( )
   commands = 'SP1;PA0,0;PD;PU;'
   p.write(commands)
   assert p.format == 'IN;' + commands


def test_plotter_write_02( ):
   '''write( ) can take a Chiplotle HPGL command.'''
   p = instantiate_virtual_plotter( )
   command = CI(1000)
   p.write(command)
   assert p.format == 'IN;' + command.format


def test_plotter_write_03( ):
   '''write( ) can take list/tuple of string HPGL commands.'''
   p = instantiate_virtual_plotter( )
   commands = ['SP2;', 'PA0,0;', 'PD;', 'PU;']
   p.write(commands)
   assert p.format == 'IN;' + ''.join(commands)


def test_plotter_write_04( ):
   '''write( ) can take list/tuple of Chiplotle HPGL commands.'''
   p = instantiate_virtual_plotter( )
   commands = [PA([(1000, 0)]), CI(500)]
   p.write(commands)
   assert p.format == 'IN;' + ''.join([c.format for c in commands])

