from chiplotle.hpgl import commands as hpgl
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl import utils

def relativize(data):
   '''Convert all absolute positions in to relative positions.'''
   result = [hpgl.PA((0,0))]
   data = utils.split_long_pen_commands(data)
   position = 0
   absolute = True
   for curr in data:
      if isinstance(curr, _Positional):
         if curr._transposable: ## it is absolute position.
            diff = curr.xy - position
            position += diff
            if isinstance(curr, hpgl.PA):
               absolute = True
               result.append(hpgl.PR(diff))
            elif isinstance(curr, hpgl.RA):
               result.append(hpgl.RR(diff))
            elif isinstance(curr, hpgl.EA):
               result.append(hpgl.ER(diff))
            elif isinstance(curr, hpgl.AA):
               result.append(hpgl.AR(diff))
         else:
            if isinstance(curr, hpgl.PR):
               absolute = False
               result.append(curr)
               position += curr.xy
            elif isinstance(curr, (hpgl.PU, hpgl.PD)):
               if len(curr.xy) > 0:
                  if absolute:
                     diff = curr.xy - position
                     command = eval('hpgl.%s()' % curr._name)
                     command.xy = diff
                     result.append(command)
                     position += diff
                  else:
                     result.append(curr)
                     position += curr.xy
               else:
                  result.append(curr)
      else:
         result.append(curr)
   return result

