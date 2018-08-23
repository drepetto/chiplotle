from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.plotters.margins.plottermargins import _PlotterMargins
from chiplotle.hpgl.commands import OW


class MarginsSoft(_PlotterMargins):
    def __init__(self, plotter):
        _PlotterMargins.__init__(self, plotter, OW())
