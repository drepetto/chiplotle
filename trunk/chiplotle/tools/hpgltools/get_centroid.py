from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.tools.hpgltools.get_all_coordinates import get_all_coordinates

def get_centroid(arg):
   '''Returns the centroid of the given Chiplotle-HPGL shapes.'''
   if isinstance(arg, _CompoundHPGL):
      arg = arg._subcommands

   arg = get_all_coordinates(arg)
   ## convert into a set to remove duplicate coordinates and to 
   ## avoid giving more weight to these duplicate points...
   arg = set(arg)
   result = CoordinatePair(0, 0)
   for c in arg:
      result += c
   return result / len(arg)
      
      
