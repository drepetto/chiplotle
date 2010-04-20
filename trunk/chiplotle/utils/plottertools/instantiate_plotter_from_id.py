from chiplotle import plotters

def instantiate_plotter_from_id(serial, id):
   '''Tries to instantiate a plotter that matches the given string `id`.
   
   - `serial` is a Serial instance.
   - `id` is a string of the plotter ID.
   '''
   ## massage id...
   id = id.replace('-', '').strip('\r')
   ## find a plotter within existing plotters that matches ID 
   ## and instantiate.
   for plt_str in dir(plotters):
      if id in plt_str:
         plotter = getattr(plotters, plt_str)(serial)
         return plotter
