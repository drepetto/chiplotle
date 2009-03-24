from chiplotle import *
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand

def test_hpglcommand_terminator_01( ):
   '''terminator is a class attribute and can be set from any instance of any
   subclass of _HPGLCommand.'''
   pu = PU( )
   pd = PD( )
   ci = CI(1)
   ar = AR((0, 0), 1)
   sc = SC( )

   assert pu.terminator == ';'
   assert pd.terminator == ';'
   assert ci.terminator == ';'
   assert ar.terminator == ';'
   assert sc.terminator == ';'
   pu.terminator = '@'
   assert pu.terminator == '@'
   assert pd.terminator == '@'
   assert ci.terminator == '@'
   assert ar.terminator == '@'
   assert sc.terminator == '@'
   ci.terminator = 2
   assert pu.terminator == 2
   assert pd.terminator == 2
   assert ci.terminator == 2
   assert ar.terminator == 2
   assert sc.terminator == 2
   ar.terminator = '#'
   assert pu.terminator == '#'
   assert pd.terminator == '#'
   assert ci.terminator == '#'
   assert ar.terminator == '#'
   assert sc.terminator == '#'

   pt = PT( )
   assert pt.terminator == '#'
   

def test_hpglcommand_terminator_02( ):
   '''terminator can not be set directly from a subclass of _HPGLCommand.'''
   pu = PU( )
   ci = CI(1)
   PD.terminator = '@'
   assert not ci.terminator == '@'
   assert not pu.terminator == '@'

def test_hpglcommand_terminator_03( ):
   '''terminator can be set directly from the _HPGLCommand private class.'''
   pu = PU( )
   ci = CI(1)
   _HPGLCommand.terminator = '@'
   assert ci.terminator == '@'
   assert pu.terminator == '@'
