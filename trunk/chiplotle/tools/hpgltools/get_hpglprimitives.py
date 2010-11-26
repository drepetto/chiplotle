from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound


def get_hpglprimitives(lst):
   '''Returns a list of _HPGLPrimitives in `lst`. If an element in `lst`
   is an _HPGLCompound, it recursively searches for the _HPGLPrimitives
   in its _subcommands property.'''
   result = [ ]
   for e in lst:
      if isinstance(e, _HPGLPrimitive):
         result.append(e)
      elif isinstance(e, _HPGLCompound):
         result += get_hpglprimitives(e._subcommands)
      else:
         raise TypeError('All elements in `lst` must be of type _HPGL.')
   return result
