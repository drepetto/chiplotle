"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.plotters.drawingplotter import _DrawingPlotter


class DXY880(_DrawingPlotter):
    def __init__(self, ser, **kwargs):
        self.allowedHPGLCommands = tuple(
            [
                "\x1b.",
                "AA",
                "AR",
                "CA",
                "CI",
                "CP",
                "CS",
                "DC",
                "DF",
                "DI",
                "DP",
                "DR",
                "DT",
                "EA",
                "ER",
                "EW",
                "FT",
                "IM",
                "IN",
                "IP",
                "IW",
                "LB",
                "LT",
                "OA",
                "OC",
                "OD",
                "OE",
                "OF",
                "OI",
                "OO",
                "OP",
                "OS",
                "OW",
                "PA",
                "PU",
                "PD",
                "PR",
                "PS",
                "PT",
                "RA",
                "RO",
                "RR",
                "SA",
                "SC",
                "SI",
                "SL",
                "SM",
                "SP",
                "SR",
                "SS",
                "TL",
                "UC",
                "VS",
                "WG",
                "XT",
                "YT",
            ]
        )
        _DrawingPlotter.__init__(self, ser, **kwargs)
        self.type = "DXY-880"
