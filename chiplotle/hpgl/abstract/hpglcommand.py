from chiplotle.hpgl.abstract.hpgl import _HPGL

class _HPGLCommand(_HPGL):
   _terminator = ';'
   
   @apply
   def terminator( ):
      def fget(self):
         return self.__class__._terminator
      def fset(self, val):
         self.__class__._terminator = val
      return property(**locals())


   @property
   def format(self):
      return '%s%s' % (self._name, self.terminator)

   ### OVERRIDES ###

   def __repr__(self):
      attributes = [ ]
      for a in dir(self):
         if not a.startswith('_'):
            if not callable(getattr(self, a)):
               if a not in ('x', 'y', 'format', 'terminator'):
                  attributes.append( '%s=%s' %(a, str(getattr(self, a))) )
      result = '%s(%s)' % (self._name, ', '.join(attributes))
      return result
