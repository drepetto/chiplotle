from chiplotle.hpgl.commands import PU
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive

def test_hpglprimitive_terminator_01( ):
   '''the _HPGLPrimitive class has a _terminator attribute that defines
   the terminator for HPGL commands. The default is `;`.'''

   assert _HPGLPrimitive._terminator == ';' 

   t = PU( )
   assert t.format == 'PU;'

   _HPGLPrimitive._terminator = '@'
   assert t.format == 'PU@'

   t = PU( )
   assert t.format == 'PU@'
   
   ## Reset terminator back to default ';' so that future
   ## tests don't fail.
   _HPGLPrimitive._terminator = ';'


