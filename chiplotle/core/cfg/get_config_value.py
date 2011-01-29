from chiplotle.core.cfg.read_config_file import read_config_file

def get_config_value(var_name):
   try:
      result = read_config_file( )[var_name]
      return result
   except KeyError:
      msg = ""
      msg +="\n* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\a\n"
      msg +="The configuration variable '%s'\n " % var_name
      msg +="could not be found in the Chiplotle configuration file. \n"
      msg +="This could be due to an update in Chiplotle that modified\n"
      msg +="the configuration parameters of the file.\n" 
      msg +="To fix,  please delete your configuration file and run\n"
      msg +="Chiplotle again.\n"
      msg +="* * * * * * * * * * * * * * * * * * * * * * * * * * * * * *\a\n"
      raise ImportError(msg)
      
