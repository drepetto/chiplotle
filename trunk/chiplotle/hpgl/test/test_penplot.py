from chiplotle.hpgl.abstract.penplot import _PenPlot
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from py.test import raises

def test_penplot_01( ):
   '''_PenPlot cannot be initialized with a flat iterable'''
   assert raises(TypeError, 'p = _PenPlot((1, 2, 3, 4))')


def test_penplot_03( ):
   '''xy cannot be set with an single number.'''
   p = _PenPlot([(1,2)])
   assert raises(TypeError, 'p.xy = 3')


def test_penplot_04( ):
   '''xy can be set with a list or tuple.'''
   p = _PenPlot([(0,0)])
   p.xy = [(1,2)]
   assert p.xy == CoordinateArray([(1,2)])
   p.xy = [(1,2),(3,4)]
   assert p.xy == CoordinateArray([(1,2),(3,4)])
   assert p.x == (1, 3)
   assert p.y == (2, 4)


def test_penplot_05( ):
   '''xy assignment must have lenth == 2*n'''
   p = _PenPlot([(0,0)])
   assert raises(TypeError, 'p.xy =(1,)')
   assert raises(TypeError, 'p.xy =(1,2,3)')


def test_penplot_06( ):
   '''xy can be set to None'''
   p = _PenPlot([(0,0)])
   p.xy = None
   assert isinstance(p.xy, CoordinateArray)
   assert len(p.xy) == 0
   assert len(p.x) == 0
   assert len(p.y) == 0


## FORMATTING ##

## TODO: these two tests work fine when py.test -x is run on this test
## flile only, but not when run on all files in directory... figure out
## why.
#def test_penplot_format_01( ):
#   '''ints format as ints.'''
#   assert _PenPlot((1, 2)).format == '_PenPlot1,2;'
#
#
#def test_penplot_format_02( ):
#   '''Floats that would normally print as Xe-n (e.g., 1e-10 instead of
#   0.0000000001) format without the 'e-n'.'''
#   assert _PenPlot((1e-12,2)).format == '_PenPlot0.00,2.00;'

