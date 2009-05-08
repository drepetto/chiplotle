from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.utils.get_base_class import get_base_class

class _HPGLCommand(_HPGL):
   _terminator = ';'
   
#   @apply
#   def terminator( ):
#      def fget(self):
#         baseclass = get_base_class(self, '_HPGLCommand')
#         return baseclass._terminator
#      def fset(self, val):
#         baseclass = get_base_class(self, '_HPGLCommand')
#         baseclass._terminator = val
#      return property(**locals())


   @property
   def format(self):
      return '%s%s' % (self._name, _HPGLCommand._terminator)

   ### OVERRIDES ###

   ### TODO: [VA] make this simpler. remove all but the name?
   def __repr__(self):
      attributes = [ ]
      for a in dir(self):
         if not a.startswith('_'):
            if not callable(getattr(self, a)):
               #if a not in ('x', 'y', 'format', 'terminator'):
               if a not in ('x', 'y', 'format'):
                  attributes.append( '%s=%s' %(a, str(getattr(self, a))) )
      result = '%s(%s)' % (self._name, ', '.join(attributes))
      return result
