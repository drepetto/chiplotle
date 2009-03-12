from chiplotle.cfg.cfg import CONFIG_FILE

def get_serial_port( ):
   '''Find user-set default serial port in the config file.'''
   try:
      f = open(CONFIG_FILE, 'r')
      lines = f.readlines( )
      f.close( )
      for l in lines:
         l.strip( )
         if l.startswith('serial_port'):
            port = l.split('=')[1].strip( )
            if port != '':
               return port
            else:
               return None
   except IOError:
      return None
