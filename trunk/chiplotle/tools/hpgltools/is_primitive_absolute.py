from chiplotle.hpgl.abstract.hpgl import _HPGL

def is_primitive_absolute(command):
   '''Returns True of `command` is a primitive HPGL with absolute position,
   False if `command` is a non-absolute position primitive HPGL. 
   Otherwise the function raises a TypeError exception.'''

   if not isinstance(command, _HPGL):
      raise TypeError('command is not an _HPGL')
   if command._name in ('AA', 'EA', 'PA', 'RA'):
      return True
   else:
      return False
