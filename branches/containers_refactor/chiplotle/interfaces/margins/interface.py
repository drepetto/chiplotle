from chiplotle.interfaces.interface import _Interface
from chiplotle.plotters.margins.marginssoft import MarginsSoft
from chiplotle.plotters.margins.marginshard import MarginsHard

class MarginsInterface(_Interface):
   
   def __init__(self, client):
      _Interface.__init__(self, client)
      self._soft = MarginsSoft(client)
      self._hard = None
      ## check if hard margin (OH) is supported by plotter...
      if 'OH' in client.allowedHPGLCommands:
         self._hard = MarginsHard(client)


   @property
   def soft(self):
      '''Read-only reference to MarginsSoft.'''
      return self._soft

   @property
   def hard(self):
      '''Read-only reference to MarginsHard.'''
      return self._hard
