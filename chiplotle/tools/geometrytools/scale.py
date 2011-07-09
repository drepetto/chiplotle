from chiplotle.geometry.core.coordinate import Coordinate

def scale(coords, value, pivot):
   '''Scales the given coordinates by the given value
   around the given pivot point.
   - `coords` is a CoordinateArray.
   - `value` is a tuple or Coordinate.
   - `pivot` is a tuple or Coordinate.
   '''
   pivot = Coordinate(*pivot)
   try: 
      ## NOTE Coordinate is a bad name for this. 
      ## Vector is a more general notion and thus more appropriate here.
      value = Coordinate(*value)
   except TypeError:
      pass

   ## TODO use matrices to make this more efficient? 
   if pivot == Coordinate(0, 0):
      coords *= value
   else:
      offset_points = coords - pivot
      scaled_points = offset_points * value
      coords = scaled_points + pivot
   return coords

