from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.tools.io.save_hpgl import save_hpgl
import os
import shutil
import subprocess

def export(expr, filename, format = 'eps'):
   '''Export Chiplotle-HPGL objects to an image file format via ``hp2xx``.

   - `expr` can be an iterable (e.g., list) of Chiplotle-HPGL objects or a
      single Chiplotle-HPGL object.
   - `filename` the file name, including path but without extension.
   - `format` is a string describing the format of the file to which the 
      Chiplotle-HPGL objects will be exported. Default is 'eps'. 
      Valid formats are: cad, dxf, em, 
      epic, eps, esc2, fig, gpt, hpgl, img, jpg, mf, nc, pbm, pcl, pcx, 
      png, pre, rgip, svg, tiff.

   .. note::
      You must have ``hp2xx`` installed before you can export Chiplote-HPGL
      objects to image files.

   '''

   save_hpgl(expr, filename)

   command = 'hp2xx -p 1 -m %s -f %s.%s %s.hpgl' % \
      (format, filename, format, filename)
   p = subprocess.Popen(command, shell = True)

   ## remove temporary HPGL file
   #os.remove(filename + '.hpgl')
