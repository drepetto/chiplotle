"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
from chiplotle.plotters.drawingplotter import _DrawingPlotter

class DPX2000(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AR','BL','CA','CC',
         'CI','CP','CS','CT','DC','DF','DI','DL','DP','DR','DT','EA','EP',
         'ER','ES','EW','FP','FS','FT','IM','IN','IP','IW','LB','LO','LT',
         'OA','OC','OD','OE','OF','OH','OI','OL','OO','OP','OS','OT','OW',
         'PA','PB','PD','PM','PU','PR','PT','RA','RO','RR','SA','SC','SI',
         'SL','SM','SP','SR','SS','TL','UC','UF','VS','WG','XT','YT'])
      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "DPX-2000"



