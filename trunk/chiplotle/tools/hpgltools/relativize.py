from chiplotle.hpgl import commands as hpgl
import numpy

## TODO: this works, but is quite ugly. Refactor!
def relativize(data):
   '''Converts all absolute coordinate commands (PA, RA, EA, AA)
   into relative commands (PR, RR, ER, AR), so that everything
   has in realtive coordinate values.'''
   ## main body...
   last_position = None
   delta = None
   result = [ ]
   for e in data:
      ## absolute...
      if isinstance(e, (hpgl.PA, hpgl.RA, hpgl.EA, hpgl.AA)):
         if isinstance(e, hpgl.PA):
            ## handle delta...
            if not last_position is None:
               delta = e.xy[0] - last_position
            last_position = e.xy[-1]
         else:
            ## handle delta...
            if not last_position is None:
               delta = e.xy - last_position
            last_position = e.xy
         result += _return_relative_from_absolute(e, delta)

      ## relative...
      elif isinstance(e, (hpgl.PR, hpgl.RR, hpgl.ER, hpgl.AR)):
         if isinstance(e, hpgl.PR):
            if not last_position is None:
               last_position += numpy.sum(e.xy, axis = 0)
            else:
               last_position = numpy.sum(e.xy, axis = 0)
            result.append(e)
         else:
            last_position = (last_position or 0) + e.xy

      else:
         result.append(e)
   return result


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


## Trash...
#def relativize(data):
#   '''Converts all absolute coordinate commands (PA, RA, EA, AA)
#   into relative commands (PR, RR, ER, AR), so that everything
#   has in realtive coordinate values.'''
#   def _return_relative_from_absolute(command, delta):
#      result = [ ]
#      if isinstance(command, hpgl.PA):
#         if delta is not None:
#            result.append(hpgl.PR(delta))
#         diff = numpy.diff(command.xy, axis=0)
#         if len(diff) > 0:
#            result.append(hpgl.PR(diff))
#      elif isinstance(command, hpgl.RA) and delta is not None:
#         result.append(hpgl.RR(delta))
#      elif isinstance(command, hpgl.EA) and delta is not None:
#         result.append(hpgl.ER(delta))
#      elif isinstance(command, hpgl.AA) and delta is not None:
#         result.append(hpgl.AR(delta))
#      return result
#
#   ## main body...
#   last_position = None
#   delta = None
#   result = [ ]
#   for e in data:
#      ## absolute...
#      if isinstance(e, (hpgl.PA, hpgl.RA, hpgl.EA, hpgl.AA)):
#         ## handle delta...
#         if not last_position is None:
#            delta = e.xy[0] - last_position
#         last_position = e.xy[-1]
#         result += _return_relative_from_absolute(e, delta)
#      ## relative...
#      elif isinstance(e, (hpgl.PR, hpgl.RR, hpgl.ER, hpgl.AR)):
#         if not last_position is None:
#            last_position += numpy.sum(e.xy, axis = 0)
#         else:
#            last_position = numpy.sum(e.xy, axis = 0)
#         result.append(e)
#      else:
#         result.append(e)
#   return result
#
