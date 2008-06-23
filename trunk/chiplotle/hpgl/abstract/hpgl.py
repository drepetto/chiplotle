
class _HPGL(object):

   @property
   def _name(self):
      return self.__class__.__name__

   @property
   def str(self):
      return self.__str__()
   
