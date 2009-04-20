"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
from chiplotle.plotters.drawingplotter import _DrawingPlotter

class HP7550A(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AF','AH','AP','AR',
         'BF','BL','CA','CC','CI','CM','CP','CS','CT','CV','DC','DF','DI',
         'DL','DP','DR','DS','DT','EA','EP','ER','ES','EW','FP','FS','FT',
         'GC','IM','IN','IP','IV','IW','KY','LB','LO','LT','NR','OA','OC',
         'OD','OE','OF','OG','OH','OI','OK','OL','OO','OP','OS','OT','OW',
         'PA','PB','PD','PG','PM','PR','PT','PU','RA','RO','RP','RR','SA',
         'SC','SI','SL','SM','SP','SR','SS','TL','UC','UF','VS','WD','WG',
         'XT','YT'])
      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "HP7550A"

