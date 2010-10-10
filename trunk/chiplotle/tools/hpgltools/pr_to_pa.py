from chiplotle.hpgl.commands import PA, PR

def pr_to_pa(arg, starting_position=None):
   '''Converts a given PR into PA starting at coordinate (0,0).'''
   if not isinstance(arg, PR):
      raise TypeError('`arg` must be of type PR');
   
   if len(arg.xy) == 0:
      return PA( )

   last_abs = starting_position or (0, 0)
   abs_coords = [last_abs]
   for p in arg.xy:
      last_abs = last_abs + p
      abs_coords.append(last_abs)
   return PA(abs_coords)
