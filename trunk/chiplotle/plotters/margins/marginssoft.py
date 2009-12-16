from chiplotle.plotters.margins.plottermargins import _PlotterMargins
from chiplotle.hpgl.commands import OW

class MarginsSoft(_PlotterMargins):
   def __init__(self, plotter):
      _PlotterMargins.__init__(self, plotter, OW( )) 


