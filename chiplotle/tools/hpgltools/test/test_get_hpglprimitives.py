from chiplotle import *
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


