from chiplotle import *
from chiplotle.plotters.margins.marginssoft import MarginsSoft
from chiplotle.tools.plottertools.instantiate_virtual_plotter import \
   instantiate_virtual_plotter

def test_marginsoft_01( ):
   '''plotter.margins.soft is an instance of MarginsSoft.'''
   p = instantiate_virtual_plotter( )
   m = p.margins.soft
   assert isinstance(m, MarginsSoft)


def test_marginsoft_02( ):
   '''MarginsSoft.bottom_left returns a Coordinate.'''
   p = instantiate_virtual_plotter( )
   m = p.margins.soft.bottom_left
   assert isinstance(m, Coordinate)


def test_marginsoft_03( ):
   '''MarginsSoft.top_right returns a Coordinate.'''
   p = instantiate_virtual_plotter( )
   m = p.margins.soft.top_right
   assert isinstance(m, Coordinate)
