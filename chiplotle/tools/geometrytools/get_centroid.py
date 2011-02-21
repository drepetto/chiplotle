
def get_centroid(coords):
   '''Returns the centroid of the given coordinates.
   
   - `coords` is a flat list of Coordinates or a CoordinateArray.
   '''

   ## convert into a set to remove duplicate coordinates...
   coords = set(coords)
   return sum(coords) / float(len(coords))
      
      
