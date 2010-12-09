from chiplotle.tools.serialtools.virtual_serial_port import VirtualSerialPort

def interactive_choose_plotter(serial):
   print "\nChoose the plotter that best fits your hardware."
   print "When in doubt choose the generic 'Plotter'."
   from chiplotle import plotters
   plotters = _get_instantiated_plotters_from_module(plotters)
   for i, plotter in enumerate(plotters):
      print '[%d] %s' % (i,  plotter.__class__.__name__)
   return plotters[int(raw_input())].__class__(serial)
   

def _get_instantiated_plotters_from_module(module):
   '''The function returns a list of instantiated plotters 
   --one per plotter type-- found in the given module. The plotters are
   instantiated with a VirtualSerialPort, for convenience and speed.
   Anything in the module that is not a plotter is removed.
   '''
   result = [ ]
   for e in dir(module):
      try:
         plotter = getattr(module, e)(VirtualSerialPort((0,0), (1, 1)))
         result.append(plotter)
      except TypeError:
         pass 
   return result
