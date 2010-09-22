
def get_base_class(instance, classname):
   '''Find the base class with name classname of given instance.''' 
   x = instance.__class__
   if isinstance(classname, str):
      while x is not None:
         if x.__name__ == classname:
            return x
         else:
            x = x.__base__
   else:
      raise ValueError('classname be must a str.')
   return False

