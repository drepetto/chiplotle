from chiplotle.cfg.read_config_file import read_config_file

def read_config_value(key):
   '''
   Read the configuration value for the given key in the config file.
   The key can be a any configuration parameter. 
   '''
   assert isinstance(key, str)
   lines = read_config_file( )
   for l in lines:
      l.strip( )
      if l.startswith(key):
         value = l.split('=')[1].strip( )
         if value != '':
            return value
         else:
            return None

