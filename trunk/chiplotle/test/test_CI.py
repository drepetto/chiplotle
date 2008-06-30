from chiplotle import *
from py.test import raises


def test_CI_01( ):
   '''CI must have at least one argument (radius).'''
   assert raises(TypeError, 'CI()')

def test_CI_02( ):
   '''CI can take only radius argument.'''
   t = CI(1)
   assert t.radius == 1

def test_CI_03( ):
   '''CI takes at most 2 arguments: radius and chord angle.'''
   t = CI(1, 90)
   assert t.radius == 1
   assert t.chordangle == 90
   assert t.format == 'CI1.0000,90;'


