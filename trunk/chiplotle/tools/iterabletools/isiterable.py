
def isiterable(data):
   try:
      iter(data)
   except TypeError:
      return False
   return True
   
