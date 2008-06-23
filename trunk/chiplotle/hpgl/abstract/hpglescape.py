from chiplotle.hpgl.abstract.hpgl import _HPGL

class _HPGLEscape(_HPGL):
   _escape = chr(27)

   @apply
   def escape( ):
      def fget(self):
         return self.__class__._escape
      def fset(self, val):
         self.__class__._escape = val
      return property(**locals())

   ### OVERRIDES ###

   def __str__(self):
      return '%s.%s' % (self.escape, self._name)

   def __repr__(self):
      return 'Escape(%s, %s)' % (repr(self.escape), self._name)

