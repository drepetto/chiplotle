from chiplotle.cfg.cfg import CONFIG_FILE
from chiplotle.cfg.verify_config_file import verify_config_file


def read_config_file( ):
   '''Read the content of the config file ``$HOME/.chiplotle/config.py``.
   Returns a dictionary of ``var : value`` entries.'''

   verify_config_file( )
   globals = { }
   locals = { }
   execfile(CONFIG_FILE, globals, locals)
   return locals

