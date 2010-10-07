
def is_flat_list(lst):
   '''Returns True if list is flat, false otherwise.'''
   if isinstance(lst, (list, tuple)):
      for e in lst:
         if isinstance(e, (list, tuple)):
            return False
      else:
         return True
   else:
      return False
