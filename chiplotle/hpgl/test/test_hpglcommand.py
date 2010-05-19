from chiplotle import *
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand

def test_hpglcommand_terminator_01( ):
   '''the _HPGLCommand class has a _terminator attribute that defines
   the terminator for HPGL commands. The default is `;`.'''

   assert _HPGLCommand._terminator == ';' 

   t = PU( )
   assert t.format == 'PU;'

   _HPGLCommand._terminator = '@'
   assert t.format == 'PU@'

   t = PU( )
   assert t.format == 'PU@'
   
   ## Reset terminator back to default ';' so that future
   ## tests don't fail.
   _HPGLCommand._terminator = ';'


