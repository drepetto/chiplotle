from chiplotle.hpgl.commands import AS, FS, PT, SP, VS

class Pen(object):
   '''The Pen class houses the following HPGL pen settable properties:
      AS, FS, SP and VS.

   - `number` : ``int`` [1 to 8] pen number.
   - `velocity` : ``int`` [1 to 60] pen velocity.
   - `force` : ``int`` pen force.
   - `acceleration` : ``int`` [1 to 4] pen velocity.
   - `thickness` : ``float`` [0.1 to 5] mm.
   '''

   def __init__(self, number, velocity=None, force=None, acceleration=None,
      thickness=None):
      
      assert isinstance(number, int)

      self.acceleration = acceleration
      self.force = force
      self.number = number
      self.velocity = velocity
      self.thickness = thickness


   @property
   def _subcommands(self):
      result = [SP(self.number)]
      if self.acceleration:
         result.append(AS(self.acceleration, self.number))
      if self.force:
         result.append(FS(self.force, self.number))
      if self.velocity:
         result.append(VS(self.velocity, self.number))
      if self.thickness:
         result.append(PT(self.thickness))
      return result


   @property
   def format(self):
      result = ''
      for c in self._subcommands:
         result += c.format
      return result

