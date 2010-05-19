from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand

def is_primitive_absolute(command):
   '''Returns True of `command` is a primitive _HPGLCommand with absolute
   position,
   False if `command` is a non-absolute position primitive _HPGLCommand. 
   Otherwise the function raises a TypeError exception.'''

   if not isinstance(command, _HPGLCommand):
      raise TypeError('command is not an _HPGLCommand')
   if command._name in ('AA', 'EA', 'PA', 'RA'):
      return True
   else:
      return False
