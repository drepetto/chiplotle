from chiplotle.hpgl import commands as hpgl
#from chiplotle.hpgl.abstract.positional import _Positional
#from chiplotle.hpgl import utils
import numpy

def relativize(data):
   '''Converts all absolute coordinate commands (PA, RA, EA, AA)
   into relative commands (PR, RR, ER, AR), so that everything
   has in realtive coordinate values.'''
   def _return_relative_from_absolute(command, delta):
      result = [ ]
      if isinstance(command, hpgl.PA):
         if delta is not None:
            result.append(hpgl.PR(delta))
         diff = numpy.diff(command.xy, axis=0)
         if len(diff) > 0:
            result.append(hpgl.PR(diff))
      elif isinstance(command, hpgl.RA) and delta is not None:
         result.append(hpgl.RR(delta))
      elif isinstance(command, hpgl.EA) and delta is not None:
         result.append(hpgl.ER(delta))
      elif isinstance(command, hpgl.AA) and delta is not None:
         result.append(hpgl.AR(delta))
      return result

   ## main body...
   last_position = None
   delta = None
   result = [ ]
   for e in data:
      ## absolute...
      if isinstance(e, (hpgl.PA, hpgl.RA, hpgl.EA, hpgl.AA)):
         ## handle delta...
         if not last_position is None:
            delta = e.xy[0] - last_position
         last_position = e.xy[-1]
         result += _return_relative_from_absolute(e, delta)
      ## relative...
      elif isinstance(e, (hpgl.PR, hpgl.RR, hpgl.ER, hpgl.AR)):
         if not last_position is None:
            last_position += numpy.sum(e.xy, axis = 0)
         else:
            last_position = numpy.sum(e.xy, axis = 0)
         result.append(e)
      else:
         result.append(e)
   return result

### TODO: trash...
#def relativize(data):
#   '''Convert all absolute positions in to relative positions.'''
#   #result = [hpgl.PA((0,0))]
#   result = [ ]
#   data = utils.split_long_pen_commands(data)
#   position = 0
#   absolute = True
#   for curr in data:
#      if isinstance(curr, _Positional):
#         if curr._transposable: ## it is absolute position.
#            diff = curr.xy - position
#            position += diff
#            if isinstance(curr, hpgl.PA):
#               absolute = True
#               result.append(hpgl.PR(diff))
#            elif isinstance(curr, hpgl.RA):
#               result.append(hpgl.RR(diff))
#            elif isinstance(curr, hpgl.EA):
#               result.append(hpgl.ER(diff))
#            elif isinstance(curr, hpgl.AA):
#               result.append(hpgl.AR(diff))
#         else:
#            if isinstance(curr, hpgl.PR):
#               absolute = False
#               result.append(curr)
#               position += curr.xy
#            elif isinstance(curr, (hpgl.PU, hpgl.PD)):
#               if len(curr.xy) > 0:
#                  if absolute:
#                     diff = curr.xy - position
#                     command = eval('hpgl.%s()' % curr._name)
#                     command.xy = diff
#                     result.append(command)
#                     position += diff
#                  else:
#                     result.append(curr)
#                     position += curr.xy
#               else:
#                  result.append(curr)
#      else:
#         result.append(curr)
#   return result


