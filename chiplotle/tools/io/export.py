from chiplotle.tools.io.save_hpgl import save_hpgl
from chiplotle.core.cfg.cfg import CONFIG_DIR
import subprocess

def export(expr, filename, fmt = 'eps'):
   '''Export Chiplotle-HPGL objects to an image file format via ``hp2xx``.

   - `expr` can be an iterable (e.g., list) of Chiplotle-HPGL objects or a
      single Chiplotle-HPGL object.
   - `filename` the file name, including path but without extension.
   - `fmt` is a string describing the format of the file to which the 
      Chiplotle-HPGL objects will be exported. Default is 'eps'. 
      Valid formats are: jpg, png, tiff and many others. 
      Please see the ``hp2xx`` documentation for details.

   .. note::
      You must have ``hp2xx`` installed before you can export Chiplote-HPGL
      objects to image files.
   '''

   htmlfile = '{0}.hpgl'.format(filename)
   imgfile  = '{0}.{1}'.format(filename, fmt)
   save_hpgl(expr, htmlfile)

   cmd = 'hp2xx --truesize -p 1 -m %s -f "%s" "%s"' % (fmt, imgfile, htmlfile)
   p = subprocess.Popen(cmd, 
                        shell  = True,
                        stdout = subprocess.PIPE, 
                        stderr = subprocess.PIPE)
   stdout, stderr = p.communicate( )

   if 'not found' in stderr:
      print _hp2xxError()
   
   return imgfile


def _hp2xxError():
   msg = '''ATTENTION: hp2xx is not installed in your system.
         hp2xx must be installed for previewing art.'''
   return msg
