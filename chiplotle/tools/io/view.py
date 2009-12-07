import os
import subprocess
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.utils.io.export import export

def view(expr):
   '''Displays Chiplotle-HPGL objects for prevewing.

   - `expr` can be an iterable (e.g., list) or a Chiplotle-HPGL object.
   '''

   ## get output dir.
   OUTPUT_DIR = '/home/vadan/.chiplotle/output'
   file_name = os.path.join(OUTPUT_DIR, 'tmp')

   ## get viewer
   PDF_VIEWER = 'evince'

   export(expr, file_name, 'eps')
   ## show!
   p = subprocess.Popen('%s %s' % (PDF_VIEWER, file_name + '.eps'), 
      shell = True)
