from chiplotle.tools.hpgltools.inflate_hpgl_string import inflate_hpgl_string
from chiplotle.hpgl import commands as hpgl
import re

def import_hpgl_file(filename, filter_commands=None):
   '''Reads a text HPGL file and "inflates" it by creating
   Chiplotle-HPGL class instances of the found HPGL commands.

   Example::

      chiplotle> square = import_hpgl_file('examples/square.hpgl')
      chiplotle> square
      [SP(pen=1), PU(xy=[ 100.  100.]), PD(xy=[ 200.  100.]), 
      PD(xy=[ 200.  200.]), PD(xy=[ 100.  200.]), 
      PD(xy=[ 100.  100.]), SP(pen=0)]
   '''

   f = open(filename)
   fs = f.read()
   f.close()

   return inflate_hpgl_string(fs, filter_commands)
