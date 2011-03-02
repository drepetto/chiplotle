from chiplotle.geometry.core.shape import _Shape

class FormatDecorator(object):
   '''FormatDecorators know how to wrap Decoratable objects with additional
   formatting stuff.

   - `sticky` = False reverts the formatting to a previous state or 
      some default.
   '''
   
   def __init__(self, sticky=False):
      self.sticky = sticky


   @property
   def preformat_commands(self):
      raise NotImplementedError

   @property
   def postformat_commands(self):
      raise NotImplementedError


   @property
   def preformat(self):
      return ''.join(self.preformat_commands.format)

   @property
   def postformat(self):
      if self.sticky:
         return ''
      else:
         return ''.join(self.postformat_commands.format)



   ## overrides ##

   def __call__(self, shape):
      if not isinstance(shape, _Shape):
         raise TypeError('Must be a Shape.')
      shape.format_decorators.append(self)

