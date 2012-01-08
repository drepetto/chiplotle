from chiplotle.tools.logtools.get_logger import get_logger

def apply_logger(f):
   '''Applies a logger object to the 'wrapped' function.'''
   logger = get_logger(f.func_name)
   f.logger = logger
   return f

