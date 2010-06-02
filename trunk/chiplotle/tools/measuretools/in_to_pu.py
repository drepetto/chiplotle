
def in_to_pu(magnitude):
   '''Converts inches to plotter units.'''
   return magnitude * 1016.0 ## == magnitude / 0.025 * 10 * 2.54
