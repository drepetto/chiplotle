##TODO: deprecate in favor of path
#from chiplotle.hpgl.compound.compound import _CompoundHPGL
#from chiplotle.hpgl.commands import PU, PD, PA
#from chiplotle.hpgl.coordinatepair import CoordinatePair
#
#class Line(_CompoundHPGL):
#   '''Line at absolute position.'''
#   def __init__(self, xy1, xy2, pen=None):
#      _CompoundHPGL.__init__(self, xy1, pen)
#      self.xy2 = CoordinatePair(xy2)
#      
#   @property
#   def _subcommands(self):
#      result = _CompoundHPGL._subcommands.fget(self)
#      result+=[PD( ),
#               PA(self.xy2),
#               PU( )]
#      return result

