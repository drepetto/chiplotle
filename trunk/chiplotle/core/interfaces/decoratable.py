
class Decoratable(object):
   
   def __init__(self):
      self.format_decorators = [ ]

   @property
   def format(self):
      '''Returns a language-specific string representation of self.'''
      path = [c.format for c in self._subcommands]
      pre_decos = [ ]
      post_decos = [ ]
      for deco in self.format_decorators:
         pre_decos.append(deco.preformat)
         post_decos.append(deco.postformat)

      pre_decos = ''.join(pre_decos)
      post_decos = ''.join(post_decos)
      path = ''.join(path)

      result = pre_decos + path + post_decos
      return result
      
