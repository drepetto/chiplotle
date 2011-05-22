from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.path import Path
import math

def arc_ellipse(width, height, 
                start_angle, end_angle, 
                segments = 100, segmentation_mode = '2PI'):  
   '''
   Constructs an arc from an ellipse with the given width, height,
   and number of segments. Arc goes from start_angle to end_angle,
   both of which are in radians.

      - `segmentation_mode` : '2PI' or 'arc'. The first segments
         the whole ellipse into the given number of segments,
         the second segments the arc.
   '''
   if start_angle > end_angle:
      end_angle += math.pi * 2
   
   def _divide_2pi():
      return (math.pi * 2) / float(segments)
   def _divide_arc():
      return (end_angle - start_angle) / float(segments)

   segmentation_map = {'2pi' : _divide_2pi,
                       'arc' : _divide_arc}

   rads_incr = segmentation_map[segmentation_mode.lower()]()
   rads = start_angle
   arc = []
   while rads < end_angle:
      coord = Coordinate(math.cos(rads), math.sin(rads))
      coord = coord * Coordinate(width / 2.0, height / 2.0)
      rads += rads_incr
      arc.append(coord)
   ## NOTE: this is better than using rads <= end_angle since
   ## the equality does not always work as expected with floats
   ## due to rounding.
   last = Coordinate(math.cos(end_angle), math.sin(end_angle))
   last *= Coordinate(width / 2.0, height / 2.0)
   arc.append(last)
   return Path(arc)


## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   from chiplotle.geometry.core.group import Group
   
   gr = Group()
   for radius in range(100, 1000, 10):
       ae = arc_ellipse(radius, radius * 2, 0, math.pi/2, 5, 'arc')
       gr.append(ae)

   io.view(gr)

