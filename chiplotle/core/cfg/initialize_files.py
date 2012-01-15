from chiplotle.core.cfg.write_config_file import write_config_file
from chiplotle.core.cfg.write_log_file import write_log_file
from chiplotle.core.cfg.cfg import LOG_FILE
from chiplotle.core.cfg.cfg import CONFIG_FILE
from chiplotle.core.cfg.cfg import CONFIG_DIR
import os

def initialize_files():
   '''Initializes all needed directories and files.'''

   output = os.path.join(CONFIG_DIR, 'output')
   if not os.path.exists(output):
      raw_input('ATTENTION: "%s" does not exist in your system.\n\
      Chiplotle will now create it to store configuration and other\n\
      session files. \n\
      (Hit Return to continue)' % CONFIG_DIR)
      os.makedirs(output)

   if not os.path.exists(LOG_FILE):
      write_log_file(LOG_FILE)

   if not os.path.exists(CONFIG_FILE):
      raw_input('ATTENTION: Chiplotle has created its configuration file\n\
      %s.\n\
      Edit this file to set various Chiplotle defaults.' % CONFIG_FILE)
      write_config_file(CONFIG_FILE)
