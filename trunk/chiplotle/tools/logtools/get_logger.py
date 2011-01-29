from chiplotle.core.cfg.cfg import LOG_FILE
from chiplotle.core.cfg.get_config_value import get_config_value
import logging

def get_logger(name):
   logger = logging.getLogger(name)
   logger.setLevel(logging.DEBUG)
   string = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
   formatter = logging.Formatter(string)
   fh = logging.FileHandler(LOG_FILE, 'w')
   fh.setLevel(logging.DEBUG)
   fh.setFormatter(formatter)
   logger.addHandler(fh)

   if get_config_value('verbose') == True:
      string = '%(name)s - %(levelname)s - %(message)s'
      formatter = logging.Formatter(string)
      s = logging.StreamHandler( )
      s.setLevel(logging.INFO)
      s.setFormatter(formatter)
      logger.addHandler(s)

   return logger
   
