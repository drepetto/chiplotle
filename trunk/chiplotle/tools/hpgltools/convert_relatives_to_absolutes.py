from chiplotle.tools.hpgltools.pens_updown_to_papr import pens_updown_to_papr
from chiplotle.tools.hpgltools.is_primitive_absolute import is_primitive_absolute
from chiplotle.tools.hpgltools.pr_to_pa import pr_to_pa
from chiplotle.geometry.core.coordinate import Coordinate
from chiplotle.geometry.core.coordinatearray import CoordinateArray
from chiplotle.hpgl.commands import PR, PA, ER, EA, RA, RR, AR, AA

def convert_relatives_to_absolutes(lst):
   if not isinstance(lst, (list, tuple)):
      raise TypeError('`lst` must be a list or tuple.')

   lst = pens_updown_to_papr(lst)

   result = [ ]
   last_position = Coordinate(0, 0)
   command = None
   for e in lst:
      ## if has absolute position, keep track of last point...
      if is_primitive_absolute(e):
         if isinstance(e.xy, CoordinateArray):
            last_position = e.xy[-1]
         else:
            last_position = e.xy

      ## handle each HPGL command type...
      if isinstance(e, PR):
         command = pr_to_pa(e, last_position)
         last_position = command.xy[-1]
      elif isinstance(e, ER):
         command = EA(last_position + e.xy)
         last_position = command.xy
      elif isinstance(e, RR):
         command = RA(last_position + e.xy)
         last_position = command.xy
      elif isinstance(e, AR):
         command = AA(last_position + e.xy, e.angle, e.chordtolerance)
         last_position = command.xy
      else:
         command = e

      result.append(command)
   return result
