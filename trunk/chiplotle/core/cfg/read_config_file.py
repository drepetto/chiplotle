from chiplotle.core.cfg.cfg import CONFIG_FILE

def read_config_file( ):
   '''Read the content of the config file ``$HOME/.chiplotle/config.py``.
   Returns a dictionary of ``var : value`` entries.'''

   globals = { }
   locals = { }
   execfile(CONFIG_FILE, globals, locals)
   return locals

