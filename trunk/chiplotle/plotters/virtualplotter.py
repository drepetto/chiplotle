"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""
from chiplotle.plotters.drawingplotter import _DrawingPlotter

'''This is a virtual plotter that uses a virtual serial port!'''

class VirtualPlotter(_DrawingPlotter):
   def __init__(self, ser, **kwargs):
      self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AR','CA','CI','CP',
         'CS','DC','DF','DI','DP','DR','DT','EA','ER','EW','FT','IM','IN',
         'IP','IW','LB','LT','OA','OC','OD','OE','OF','OH','OI','OO','OP',
         'OS','OW','PA','PU','PD','PR','PS','PT','RA','RO','RR','SA','SC',
         'SI','SL','SM','SP','SR','SS','TL','UC','VS','WG','XT','YT'])
      _DrawingPlotter.__init__(self, ser, **kwargs)
      self.type = "Virtual"
      self._serial_port = ser

   @property
   def format(self):
      '''This lets us pass the VirtualPlotter directly to io.view()'''
      return self._serial_port.format