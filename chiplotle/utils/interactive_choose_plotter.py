from chiplotle import plotters

def interactive_choose_plotter(serial_port):
   tmp_plotter = plotters.Plotter(serial_port)
   id = tmp_plotter.id
   print "Found plotter with ID: %s" % id
   ## try to instantiate a plotter that matches found ID...
   for plt_str in dir(plotters):
      if id in plt_str:
         plotter = getattr(plotters, plt_str)(serial_port)
         print "Instantiated plotter %s" % plotter
         return plotter
   ## not found, choose manually...
   else:
      print "ATTENTION: Plotter %s not supported." % id

      print "Choose the plotter that best fits your hardware."
      print "If in doubt choose the generic 'Plotter'."
      for i, plotter in enumerate(dir(plotters)):
         print '[%d] %s' % (i,  plotter)
      plt_name = dir(plotters)[int(raw_input())]
      plotter = getattr(plotters, plt_name)(serial_port)
      return plotter
   
#   plotter = plotters.Plotter(serial_port)
#   print "\nFound plotter ID: %s." % plotter.id
#   print "\nChoose a plotter type:"
#   for i, plotter in enumerate(dir(plotters)):
#      print '[%d] %s' % (i,  plotter)
#   #plotter = plotters.__dict__[ dir(plotters)[int(raw_input())] ](serial_port)
#   plt_name = dir(plotters)[int(raw_input())]
#   plotter = getattr(plotters, plt_name)(serial_port)
#   return plotter
