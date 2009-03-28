from chiplotle import plotters

def write_config_file(path):
   f = open(path, 'w')
   answer = _ask_serial_port( )
   f.write('serial_port=%s\n' % answer)
   answer = _ask_plotter_type( )
   f.write('plotter_type=%s\n' % answer)
   f.close( )


def _ask_serial_port( ):
   print "You can set a default serial port for Chiplotle to use every time it is run in live scripting mode. In POSIX type operating systems these ports are under the /dev directory. Serial ports usually look like ttyS0, ttyS1, etc. If you have a computer with no serial port and you are using a serial to USB converter then these ports typically look like ttyUSB0, ttyUSB1, etc. If you know what port your plotter is connected to you can set it as a default now so you don't have to tell Chiplotle what port to use every time you run it. If you don't know what port to use you can skip this setting and Chiplotle will ask you what port to use every time you run it live. You can always modify your default settings by editing the $HOME/.chiplotle/config file."
   sp = raw_input('Enter the FULL PATH to your serial port or hit Enter for default [None]:')
   return sp


def _ask_plotter_type( ):
   plotter_list = ''
   for i, plotter in enumerate(dir(plotters)):
      plotter_list += '[%d] %s\n' % (i+1,  plotter)
   message = '\nSet the default plotter type. Plotter types available are:\n%s\n' % plotter_list
   print message
   answer = raw_input('Enter the plotter number to set as default or hit Enter [None]:\n')
   plt_name = dir(plotters)[int(answer)-1]
   return plt_name
