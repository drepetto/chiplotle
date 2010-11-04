from chiplotle.tools.logtools.get_logger import get_logger

def apply_logger(f):
   '''Applies a logger object to the 'wrapped' function.'''
   logger = get_logger(f.func_name)
   f.logger = logger
   return f


#class applyLogger(object):
#
#   def __init__(self, f):
#      self.f = f
#      # need this?
#      #self.__name__ = f.__name__
#
#
#   def __call__(self):
#      from chiplotle.tools.logtools.get_logger import get_logger
#      logger = get_logger(f.func_name)
#      ## how would f access logger from within itself?
#      f.logger = logger
#      self.f( )
      
