from chiplotle.tools.io.save_hpgl import save_hpgl
from chiplotle.cfg.cfg import CONFIG_DIR
from chiplotle.cfg._verify_output_directory import _verify_output_directory
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

   _verify_output_directory( )
   temp_file = os.path.join(CONFIG_DIR, 'output', 'tmp.hpgl')
   save_hpgl(expr, temp_file)

   command = 'hp2xx -p 1 -m %s -f %s.%s %s' % \
      (format, filename, format, temp_file)
   p = subprocess.Popen(command, shell = True,
      stdout = subprocess.PIPE, stderr = subprocess.PIPE)
   stdout, stderr = p.communicate( )
   #print 'hp2xx output:'
   #print 'stdout:', stdout
   #print 'stderr:', stderr
   if 'not found' in stderr:
      print 'ATTENTION: hp2xx is not installed in your system.'
      print '\thp2xx must be installed for export( ) and view( )'
      print '\tto work.'
      
