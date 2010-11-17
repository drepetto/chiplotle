from chiplotle.hpgl.compound.decorators.hpglcompounddecorator \
   import _HPGLCompoundDecorator
from chiplotle.hpgl.commands import AS, FS, PT, SP, VS

class DPen(_HPGLCompoundDecorator):
   '''The Pen class houses the following HPGL pen settable properties:
      AS, FS, SP and VS.

   - `number` : ``int`` [1 to 8] pen number.
   - `velocity` : ``int`` [1 to 60] pen velocity.
   - `force` : ``int`` pen force.
   - `acceleration` : ``int`` [1 to 4] pen velocity.
   - `thickness` : ``float`` [0.1 to 5] mm.
   '''

   def __init__(self, hpglcompound, number, velocity=None, force=None, 
      acceleration=None, thickness=None, hold_state=False):
      
      _HPGLCompoundDecorator.__init__(self, hpglcompound)

      self.acceleration = acceleration
      self.force = force
      self.number = number
      self.velocity = velocity
      self.thickness = thickness
      self.hold_state = hold_state


   @property
   def _pre_decorator_subcommands(self):
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
   def _post_decorator_subcommands(self):
      if not self.hold_state:
         return [SP( ), AS( ), FS( ), VS( ), PT( )]
      else:
         return [ ]

   @property
   def _subcommands(self):
      result = self._pre_decorator_subcommands
      result += self.hpglcompound._subcommands
      result += self._post_decorator_subcommands
      return result
