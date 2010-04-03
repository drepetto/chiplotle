from chiplotle.plotters.drawingplotter import _DrawingPlotter

class HP7585B(_DrawingPlotter):
   '''Use with Houston Instruments DMP-60.'''
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AP','AR',
         'AS','BL','CA','CI','CP','CS','CT','CV','DC','DF',
         'DI','DP','DR','DT','EA','EP','ER','ES','EW','FP',
         'FT','GC','GM','GP','IM','IN','IP','IW','KY',
         'LB','LO','LT','NR','OA','OB','OC','OD','OE','OF','OG','OH','OI',
         'OK','OL','OO','OP','OS','OT','OW','PA','PB','PD','PM','PR',
         'PT','PU','RA','RL','RO','RR','SA','SC','SG','SI','SL','SM',
         'SP','SR','SS','TL','UF','VS','WG','XT','YT'])

      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "HP7585B"

