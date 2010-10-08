from chiplotle.tools.iterabletools.isiterable import isiterable

def ispair(data):
   return (isiterable(data) and len(data) == 2)

