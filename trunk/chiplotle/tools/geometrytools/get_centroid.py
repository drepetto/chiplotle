from chiplotle.geometry.coordinate import Coordinate

def get_centroid(coords):
   '''Returns the centroid of the given coordinates.
   
   - `coords` is a flat list of Coordinates or a CoordinateArray.
   '''

   ## convert into a set to remove duplicate coordinates...
   coords = set(coords)
   result = Coordinate(0, 0)
   for c in coords:
      result += c
   return result / len(coords)
      
      
