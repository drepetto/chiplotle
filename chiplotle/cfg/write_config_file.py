from chiplotle import plotters
import time


def write_config_file(path):
   ## get some values from user...
#   serial_port = _ask_serial_port( )

   ## set preamble...
   preamble = '# -*- coding: utf-8 -*-\n'
   preamble += '# \n'
   preamble += '# Chiplotle configuration file.\n'
   preamble += '# Created by Chiplotle on %s.\n' % time.strftime("%d %B %Y %H:%M:%S")
   preamble += '#\n'
   preamble += '# This file houses all the configuration variables employed\n'
   preamble += '# by Chiplotle. You can set them manually to suit your needs.\n'
   preamble += '# Do not delete them! If you want them to have no effect\n'
   preamble += '# simply set them to "None".\n'
   preamble += '#\n'
   preamble += '# This file is executed via the ``execfile( )`` function,\n'
   preamble += "# so all its content should adhere to the Python syntax.\n"
   preamble += '\n\n'

   ## write file...
   f = open(path, 'w')

   f.write(preamble)

   f.write("# Configuration Variables ---------------------------------\n\n")

#   f.write("# Serial port to use for all connections.\n")
#   f.write("# Set it to a string of the path to the port (e.g., '/dev/ttyUSB0'),\n")
#   f.write("# an integer port number or `None` to have Chiplotle query you.'\n")
#   if serial_port:
#      f.write("serial_port = '%s'" % serial_port)
#   else:
#      f.write("serial_port = None")
#   f.write("\n\n")

   ## default serial parameters...
   f.write("# Serial connection parameters (default).\n")
   f.write("baudrate = 9600\n")
   f.write("bytesize = 8\n")
   f.write("parity = 'N'\n")
   f.write("stopbits = 1\n")
   f.write("timeout = 1\n")
   f.write("xonxoff = 1\n")
   f.write("rtscts = 0\n")
   f.write("\n\n")

#   f.write("# PDF viewer. Set for previewing HPGL commands via the\n")
#   f.write("# ``view( )`` function. If set to `None`, the viewer will\n")
#   f.write("# use the OS dependent generic file opener.\n")
#   f.write("# e.g., `open` in OS X, `xdg-open` in Linux.\n")
#   f.write("pdf_viewer = None")
#   f.write('\n\n')

   f.close( )


## HELPER FUNCTIONS ##

def _ask_serial_port( ):
   print "* Serial port *"
   print "You can set a default serial port for Chiplotle to use every time it is run in live scripting mode. In POSIX type operating systems these ports are under the /dev directory. Serial ports usually look like ttyS0, ttyS1, etc. If you have a computer with no serial port and you are using a serial to USB converter then these ports typically look like ttyUSB0, ttyUSB1, etc. If you know what port your plotter is connected to you can set it as a default now so you don't have to tell Chiplotle what port to use every time you run it. If you don't know what port to use you can skip this setting and Chiplotle will ask you what port to use every time you run it live. You can always modify your default settings by editing the $HOME/.chiplotle/config.py file."
   sp = raw_input('Enter the FULL PATH of your serial port or hit Enter for None:')
   if sp == '':
      return None
   else:
      return sp

