from chiplotle.cfg.cfg import CONFIG_FILE, CONFIG_DIR
from chiplotle.cfg.write_config_file import write_config_file
import os

def verify_config_file( ):
   try:
      f = open(CONFIG_FILE, 'r')
      f.close( )
   except IOError:
      raw_input('Attention: "%s" does not exist in your system.\n\
      Chiplotle will now create it to store all configuration settings. \n\
      Press any key to continue.' % CONFIG_FILE)
      if not os.path.isdir(CONFIG_DIR):
         os.mkdir(CONFIG_DIR)
      write_config_file(CONFIG_FILE)
