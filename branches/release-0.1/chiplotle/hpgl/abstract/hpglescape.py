from chiplotle.hpgl.abstract.hpgl import _HPGL
from chiplotle.utils.get_base_class import get_base_class

## TODO replace .escape object property refering to the _escape
## class property with just the _escape class property.
class _HPGLEscape(_HPGL):
   _escape = chr(27)

   @apply
   def escape( ):
      def fget(self):
         baseclass = get_base_class(self, '_HPGLEscape')
         return baseclass._escape
      def fset(self, val):
         baseclass = get_base_class(self, '_HPGLEscape')
         baseclass._escape = val
      return property(**locals())


   @property
   def format(self):
      return '%s.%s' % (self.escape, self._name)

   ### OVERRIDES ###

   def __repr__(self):
      return 'Escape(%s, %s)' % (repr(self.escape), self._name)

