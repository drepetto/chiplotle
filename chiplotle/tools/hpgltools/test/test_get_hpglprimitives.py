from chiplotle import *
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.tools.hpgltools.get_hpglprimitives import get_hpglprimitives
from py.test import raises


def test_get_hpglprimitives_01( ):
   '''The argument must be an iterable.'''
   assert raises(TypeError, 'get_hpglprimitives(3)')


def test_get_hpglprimitives_02( ):
   '''Only _HPGL instances are allowed.'''
   assert raises(TypeError, 'get_hpglprimitives([PU( ), 3])')


def test_get_hpglprimitives_03( ):
   '''HPGLPrimitives are returned unharmed.'''
   d = [PU( ), PA((1,2,3,4)), PD( ), ER((1, 2))]
   t = get_hpglprimitives(d)
   assert t == d


def test_get_hpglprimitives_04( ):
   '''The function can take both _HPGLPrimitives and _HPGLCompound objects.'''
   d = [Circle((0, 0), 300), PU( ), PA((1, 2))]
   t = get_hpglprimitives(d)
   assert t == [PU( ), PA((0, 0)), CI(300), PU( ), PA((1, 2))]


def test_get_hpglprimitives_05( ):
   '''get_hpglprimitives( ) acts recursively. i.e., HPGLCompound shapes
   that return HPGLCompound shapes as _subcommands are also processed
   for _HPGLPrimitive commands retrieval.'''
   d = [RoundRectangle((0, 0), 100, 200)]
   t = get_hpglprimitives(d)
   for e in t:
      assert isinstance(e, _HPGLPrimitive)
