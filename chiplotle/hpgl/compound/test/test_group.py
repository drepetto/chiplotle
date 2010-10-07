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


## list-like operators ##

def test_group_append_01( ):
   '''_HPGL objects can be appended.'''
   g = Group((1, 2), [PU( )])
   g.append(PD( ))
   assert len(g) == 2
   assert g[1] == PD( )
   assert g._subcommands == [PU( ), PA((1, 2)), PU( ), PD( )]


def test_group_append_02( ):
   '''Group checks that the appended object is _HTML type.'''
   g = Group((1, 2), [PU( )])
   assert raises(TypeError, "g.append('PU')")



def test_group_extend_01( ):
   g = Group((1, 2), [PU( )])
   g.extend([PD( )])
   assert len(g) == 2
   assert g[1] == PD( )
   assert g._subcommands == [PU( ), PA((1, 2)), PU( ), PD( )]


def test_group_extend_02( ):
   '''Group checks that each of the objects in the extend list is _HTML type.'''
   g = Group((1, 2), [PU( )])
   assert raises(TypeError, "g.extend(['PU', 'PD'])")


def test_group_insert_01( ):
   g = Group((1, 2), [CI(500), CI(200)])
   g.insert(1, ER((400, 400)))
   assert len(g) == 3
   assert g[1] == ER((400, 400))


def test_group_insert_02( ):
   '''insert checks for _HTML type.'''
   g = Group((1, 2), [PU( )])
   assert raises(TypeError, "g.insert(1, 'PU')")


def test_group_remove_01( ):
   g = Group((1, 2), [CI(200), CI(300)])
   r = g.remove(CI(200))
   assert r is None
   assert len(g) == 1
   assert g[0] == CI(300)


def test_group_pop_01( ):
   g = Group((1, 2), [CI(200), CI(300)])
   r = g.pop(1)
   assert r == CI(300)
   assert len(g) == 1
   assert g[0] == CI(200)

   
## overrides ##

def test_group__delitiem__01( ):
   g = Group((1, 2), [CI(200), CI(300)])
   del(g[0])
   assert len(g) == 1
   assert g[0] == CI(300)
   

def test_group__getitem__01( ):
   g = Group((1, 2), [CI(200), CI(300)])
   assert g[0] == CI(200)
   assert g[1] == CI(300)


def test_group__setitem__01( ):
   g = Group((1, 2), [CI(200), CI(300)])
   g[0] = ER((100, 100))
   assert len(g) == 2
   assert g[0] == ER((100, 100))
   assert g[1] == CI(300)
   

def test_group__setitem__02( ):
   g = Group((1, 2), [CI(200), CI(300), CI(400)])
   g[0:2] = [ER((100, 100))]
   assert len(g) == 2
   assert g[0] == ER((100, 100))
   assert g[1] == CI(400)
   
