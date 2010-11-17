from chiplotle.hpgl.compound.hpglcompound import _HPGLCompound


class _HPGLCompoundDecorator(_HPGLCompound):
   '''Abstract clas for HPGLCompound Decorators.

   Interface (must implement):
      - `_subcommands`
   '''

   def __init__(self, hpglcompound):
      self.hpglcompound = hpglcompound


   @apply
   def xy( ):
      def fget(self):
         return self.hpglcompound._coords
      def fset(self, arg):
         self.hpglcompound._coords = CoordinatePair(arg)
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self.hpglcompound._coords.x
      def fset(self, arg):
         self.xy = CoordinatePair(arg, self.y)
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self.hpglcompound._coords.y
      def fset(self, arg):
         self.xy = CoordinatePair(self.x, arg)
      return property(**locals())


   ## PRIVATE PROPERTIES ##


#   @property
#   def _decorated_chain(self):
#      if isinstance(self.hpglcompound, _HPGLCompoundDecorator):
#         result = [self] + self._decorated_chain
#      else:
#         result = [self, self.hpglcompound]
#      return result


   ## OVERRIDES ##
   
   def __repr__(self):
      return str(self)

   def __str__(self):
      return '%s(%s)' % (self._name, self.hpglcompound)

