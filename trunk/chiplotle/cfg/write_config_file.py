from chiplotle import plotters
import time


def write_config_file(path):

   ## write file...
   f = open(path, 'w')

   ## set preamble...
   preamble = '# -*- coding: utf-8 -*-\n'
   preamble += '## \n'
   preamble += '## Chiplotle configuration file.\n'
   preamble += '## Created by Chiplotle on %s.\n' % time.strftime("%d %B %Y %H:%M:%S")
   preamble += '##\n'
   preamble += '## This file houses all the configuration variables employed\n'
   preamble += '## by Chiplotle. You can set them manually to suit your needs.\n'
   preamble += '## Do not delete them! If you want them to have no effect\n'
   preamble += '## simply set them to "None".\n'
   preamble += '##\n'
   preamble += '## This file is executed via the ``execfile( )`` function,\n'
   preamble += "## so all its content should adhere to the Python syntax.\n"
   preamble += '\n\n'
   f.write(preamble)

   f.write("# Configuration Variables ---------------------------------\n\n")

   ## serial port to plotter mappings...
   f.write("## Serial ports to plotters map.\n")
   f.write("## Set to None if you want Chiplotle to dynamically find the\n")
   f.write("## plotters connected to your computer. This is the default.\n")
   f.write("## This default is convenient when your setup changes frequently.\n")
   f.write("## For a fixed setup set this to a dictionary mapping serial\n")
   f.write("## ports to plotters. \n")
   f.write("## e.g., {'/dev/ttyS0' : 'DXY-1300', '/dev/ttyS1' : 'HP7475A'}\n")
   f.write("## sets plotter 'DXY-1300' to port '/dev/ttyS0' and plotter\n")
   f.write("## 'HP7475A' to port '/dev/ttyS1'.\n")
   f.write("serial_port_to_plotter_map = None\n")
   f.write("\n\n")

   ## default serial parameters...
   f.write("## Serial connection parameters.\n")
   f.write("## Set your plotter to match these values, or vice versa..\n")
   f.write("baudrate = 9600\n")
   f.write("bytesize = 8\n")
   f.write("parity = 'N'\n")
   f.write("stopbits = 1\n")
   f.write("timeout = 1\n")
   f.write("xonxoff = 1\n")
   f.write("rtscts = 0\n")
   f.write("\n\n")

#   f.write("## PDF viewer. Set for previewing HPGL commands via the\n")
#   f.write("## ``view( )`` function. If set to `None`, the viewer will\n")
#   f.write("## use the OS dependent generic file opener.\n")
#   f.write("## e.g., `open` in OS X, `xdg-open` in Linux.\n")
#   f.write("pdf_viewer = None")
#   f.write('\n\n')

   f.close( )


## TRASH...
### HELPER FUNCTIONS ##
#
#def _ask_serial_port( ):
#   print "* Serial port *"
#   print "You can set a default serial port for Chiplotle to use every time it is run in live scripting mode. In POSIX type operating systems these ports are under the /dev directory. Serial ports usually look like ttyS0, ttyS1, etc. If you have a computer with no serial port and you are using a serial to USB converter then these ports typically look like ttyUSB0, ttyUSB1, etc. If you know what port your plotter is connected to you can set it as a default now so you don't have to tell Chiplotle what port to use every time you run it. If you don't know what port to use you can skip this setting and Chiplotle will ask you what port to use every time you run it live. You can always modify your default settings by editing the $HOME/.chiplotle/config.py file."
#   sp = raw_input('Enter the FULL PATH of your serial port or hit Enter for None:')
#   if sp == '':
#      return None
#   else:
#      return sp
#
