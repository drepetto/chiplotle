import os
import subprocess
from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.tools.io.export import export
from chiplotle.tools.io._open_file import _open_file

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
   _open_file(file_name + '.eps')
   #p = subprocess.Popen('%s %s' % (PDF_VIEWER, file_name + '.eps'), 
   #   shell = True)
