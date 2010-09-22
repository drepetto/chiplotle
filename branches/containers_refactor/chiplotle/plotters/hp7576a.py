from chiplotle.plotters.drawingplotter import _DrawingPlotter

class HP7576A(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      ## allowedHPGLCommands must be set prior to base class init.
      self.allowedHPGLCommands = tuple(['\x1b.','AA','AP','AR','CA','CI',
         'CM','CP','CS','CT','DC','DF','DI','DP','DR','DS','DT','DV','EA',
         'EP','ER','ES','EW','FP','FT','IM','IN','IP','IV','IW','LB','LO',
         'LT','NR','OA','OC','OD','OE','OF','OH','OI','OO','OP','OS','OT',
         'OW','PA','PD','PM','PR','PS','PT','PU','RA','RO','RR','SA','SC',
         'SI','SL','SM','SP','SR','SS','TL','UC','VS','WG','XT','YT'])

      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "HP7576A"

