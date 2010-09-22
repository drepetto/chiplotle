from chiplotle import *
from py.test import raises

def test_group_01( ):
   '''Group must initialize with a position always.'''
   assert raises(TypeError, 'g = Group( )')


def test_group_02( ):
   '''A Group can be empty, but always has an "absolute" position.'''
   g = Group((1, 2))

   assert len(g) == 0
   assert g._subcommands == [PU( ), PA((1, 2))]
   assert g.format == 'PU;PA1,2;'


def test_group_03( ):
   '''Group can take any object of type _HPGL, i.e. _HPGLPrimitives as well
   as CompoundHPGL commands.'''
   g = Group((1, 2), [PD( ), Circle((10, 10), 100)])

   assert len(g) == 2
   

def test_group_04( ):
   '''Group cannot take any object other than _HPGL types.'''
   assert raises(TypeError, 'g = Group((1, 2), [PD( ), 3])')


## HPGLPrimitive handling ##

def test_group_primitive_01( ):
   '''Groups can take HPGL primitives.'''
   g = Group((1, 2), [PD( ), PA((10, 10))])

   assert len(g) == 2
   ## The subcommands with absolute positional attribute xy are returned
   ## with the attribute adjusted to reflect the Group's position.
   assert g._subcommands == [PU( ), PA((1, 2)), PD( ), PA((11, 12))]
   assert g.format == 'PU;PA1,2;PD;PA11,12;'


def test_group_primitive_02( ):
   '''HPGL primitives with absolute positioning contained in a Group are
   displaced relative to the Group's position when returned by 
   g._subcommands. HPGL primitives with relative positioning are left 
   unadjusted.'''
   g = Group((1, 2), [PR((10, 10)), ER((100, 100)), EA((100, 100)), PA((10, 10))])

   assert len(g) == 4
   ## The subcommands with absolute positional attribute xy are returned
   ## with the attribute adjusted to reflect the Group's position.
   assert g._subcommands == [PU( ), PA((1, 2)), PR((10, 10)), ER((100, 100)), 
      EA((101, 102)), PA((11, 12))]
   assert g.format == 'PU;PA1,2;PR10,10;ER100,100;EA101,102;PA11,12;'


