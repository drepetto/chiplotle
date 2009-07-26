from chiplotle.cfg.cfg import CONFIG_FILE, CONFIG_DIR
from chiplotle.cfg.write_config_file import write_config_file
import os

def verify_config_file( ):
   try:
      f = open(CONFIG_FILE, 'r')
      f.close( )
   except IOError:
      print 'ATTENTION: "%s" does not exist in your system.\nChiplotle will now create it to store all configuration settings.\nEdit this file to modify Chiplotle default values.' % CONFIG_FILE
      raw_input('Press any key to continue...\n')
      if not os.path.isdir(CONFIG_DIR):
         os.mkdir(CONFIG_DIR)
      write_config_file(CONFIG_FILE)
