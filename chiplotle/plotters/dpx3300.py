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

class DPX3300(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AR','BL','CA','CC',
         'CI','CP','CS','CT','DC','DF','DI','DL','DP','DR','DT','EA','EP',
         'ER','ES','EW','FP','FS','FT','IM','IN','IP','IW','LB','LO','LT',
         'OA','OC','OD','OE','OF','OH','OI','OL','OO','OP','OS','OT','OW',
         'PA','PB','PD','PM','PU','PR','PT','RA','RO','RR','SA','SC','SI',
         'SL','SM','SP','SR','SS','TL','UC','UF','VS','WG','XT','YT'])
      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "DPX-3300"

