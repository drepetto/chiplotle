from chiplotle.geometry.core.shape import _Shape

class FormatDecorator(object):
   '''FormatDecorators know how to wrap Shape objects with additional
   formatting stuff.
   '''
   
   @property
   def _subcommands(self):
      raise NotImplementedError


   ## overrides ##

   def __call__(self, shape):
      if not isinstance(shape, _Shape):
         raise TypeError('Must be a Shape.')
      #shape.formatters.append(self)
      shape.formatters.add(self)

