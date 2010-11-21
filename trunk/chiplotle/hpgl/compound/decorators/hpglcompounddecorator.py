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
         return self.hpglcompound.xy
      def fset(self, arg):
         self.hpglcompound.xy = arg
      return property(**locals())

   @apply
   def x( ):
      def fget(self):
         return self.hpglcompound.x
      def fset(self, arg):
         self.hpglcompound.x = arg
      return property(**locals())

   @apply
   def y( ):
      def fget(self):
         return self.hpglcompound.y
      def fset(self, arg):
         self.hpglcompound.y = arg
      return property(**locals())


   ## PRIVATE PROPERTIES ##



   ## OVERRIDES ##
   
   def __repr__(self):
      return str(self)

   def __str__(self):
      return '%s(%s)' % (self._name, self.hpglcompound)

