from chiplotle.geometry.coordinate import Coordinate

def get_centroid(arg):
   '''Returns the centroid of the given coordinates.
   
   - `arg` is a flat list of Coordinates or a CoordinateArray.
   '''

   ## convert into a set to remove duplicate coordinates...
   arg = set(arg)
   result = Coordinate(0, 0)
   for c in arg:
      result += c
   return result / len(arg)
      
      
