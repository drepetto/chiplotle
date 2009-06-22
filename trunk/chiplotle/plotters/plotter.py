from chiplotle.plotters.drawingplotter import _DrawingPlotter

class Plotter(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      ## allowedHPGLCommands must be set prior to base class init.
      self.allowedHPGLCommands = tuple(['\x1b.','AA','AR','CA','CI','CP',
         'CS','DC','DF','DI','DP','DR','DT','EA','ER','EW','FT','IM','IN',
         'IP','IW','LB','LT','OA','OC','OD','OE','OF','OH','OI','OO','OP',
         'OS','OW','PA','PD','PR','PS','PT','PU','RA','RO','RR','SA','SC',
         'SI','SL','SM','SP', 'SR','SS','TL','UC','VS','WG','XT','YT'])

      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "Generic"

