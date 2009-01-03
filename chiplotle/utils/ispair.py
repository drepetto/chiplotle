from chiplotle.utils.isiterable import isiterable

def ispair(data):
   return (isiterable(data) and len(data) == 2)

