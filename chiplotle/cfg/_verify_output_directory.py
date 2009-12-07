import os
from chiplotle.cfg.cfg import CONFIG_DIR

def _verify_output_directory(directory = None):
   directory = directory or os.path.join(CONFIG_DIR, 'output')
   if not os.path.isdir(directory):
      raw_input('Attention: "%s" does not exist in your system.\n\
      Chiplotle will now create it to store all generated output files. \n\
      Press any key to continue.' % directory)
      os.makedirs(directory)
