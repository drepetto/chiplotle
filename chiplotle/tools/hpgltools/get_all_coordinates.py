from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound
from chiplotle.geometry.coordinatearray import CoordinateArray
from chiplotle.tools.hpgltools.convert_relatives_to_absolutes import \
   convert_relatives_to_absolutes


def get_all_coordinates(arg):
   '''Returns all absolute coordinates for a given list of Chiplotle-HPGL commands.
   
   Example::

      >>> t = [PA((1, 2)), PR((1, 1)), ER((1, 1)), CI(100)]
      >>> c = hpgltools.get_all_coordinates(t)
      >>> print c
      [CP(1, 2), CP(2, 3), CP(3, 4)]
   '''
   if isinstance(arg, _HPGLCompound):
      arg = arg._subcommands
   elif not isinstance(arg, (list, tuple)):
      raise TypeError('`arg` must be list, tuple or _HPGLCompound')

   arg = convert_relatives_to_absolutes(arg)

   result = [ ]
   for e in arg:
      if isinstance(e, _HPGLPrimitive) and hasattr(e, 'xy'):
         if isinstance(e.xy, CoordinateArray):
            result.extend(e.xy)
         else:
            result.append(e.xy)
      elif isinstance(e, _HPGLCompound):
         result += get_all_coordinates(e._subcommands)
   return result
