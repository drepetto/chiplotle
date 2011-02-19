
class Decoratable(object):
   
   def __init__(self):
      self.format_decorators = [ ]

   @property
   def _prefix_commands(self):
      result = [ ]
      for deco in self.format_decorators:
         result += deco.preformat_commands
      return result


   @property
   def _infix_commands(self):
      raise NotImplementedError

   @property
   def _suffix_commands(self):
      result = [ ]
      for deco in reversed(self.format_decorators):
         result += deco.postformat_commands
      return result

   @property
   def _subcommands(self):
      '''Returns a list of language-specific commands representing self.'''
      result = \
         self._prefix_commands + \
         self._infix_commands + \
         self._suffix_commands
      return result
      

   @property
   def format(self):
      '''Returns a language-specific string representation of self.'''
      return ''.join([c.format for c in self._subcommands])
