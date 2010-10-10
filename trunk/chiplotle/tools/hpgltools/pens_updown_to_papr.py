from chiplotle.hpgl.commands import PA, PR, PU, PD

def pens_updown_to_papr(lst):
   '''Converts all PU and PD found in `lst` into (PA, PU) pair sequences.
   The function removes the coordinates from PU and PD and places them in
   PR or PA, whatever was last found in lst.'''

   if not isinstance(lst, (list, tuple)):
      raise TypeError('`lst` argument must be a list or tuple.')

   result = [ ]
   last_penplot = None
   for e in lst:
      if isinstance(e, (PU, PD)):
         if len(e.xy) > 0:
            ## what to do if there is no PA or PR before a PU or PD with 
            ## coordinates? Is there a default?
            if last_penplot is None:
               msg = "*** WARNING: %s with coordinates found without prior PA or PR. PA assumed." % e
               print(msg)
               last_penplot = PA( )
            last_penplot.xy = e.xy
            e.xy = None
            result.append(e)
            result.append(last_penplot)
         else:
            result.append(e)
      else:
         if isinstance(e, PR):
            last_penplot = PR( )
         elif isinstance(e, PA):
            last_penplot = PA( )
         result.append(e)

   return result

