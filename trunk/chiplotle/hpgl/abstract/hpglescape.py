from chiplotle.hpgl.abstract.hpgl import _HPGL

class _HPGLEscape(_HPGL):

   _escape = chr(27)


   ## PUBLIC PROPERTIES ##

   @property
   def format(self):
      return '%s.%s' % (self._escape, self._name)


   ## OVERRIDES ##

   def __repr__(self):
      return 'Escape(%s, %s)' % (repr(self._escape), self._name)

