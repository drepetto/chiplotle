from chiplotle.hpgl.commands import AS, FS, PT, SP, VS

class PenDefaults(object):
   '''Sets Pen related parameters to hardware plotter defaults, for all pens.'''

   @property
   def _subcommands(self):
      return [AS( ), FS( ), VS( ), PT( ), SP(1)]


   @property
   def format(self):
      return ''.join([c.format for c in self._subcommands])

