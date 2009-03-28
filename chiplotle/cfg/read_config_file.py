from chiplotle.cfg.cfg import CONFIG_FILE
from chiplotle.cfg.verify_config_file import verify_config_file

def read_config_file( ):
   '''Read the content of the config file $HOME/.chiplotle/config.'''
   verify_config_file( )
   f = open(CONFIG_FILE, 'r')
   lines = f.readlines( )
   f.close( )
   return lines
