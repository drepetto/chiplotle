from chiplotle import plotters

def interactive_choose_plotter(serial_port):
   plotter = plotters.Plotter(serial_port)
   print "\nFound plotter ID: %s." % plotter.id
   print "\nChoose a plotter type:"
   for i, plotter in enumerate(dir(plotters)):
      print '[%d] %s' % (i,  plotter)
   #plotter = plotters.__dict__[ dir(plotters)[int(raw_input())] ](serial_port)
   plt_name = dir(plotters)[int(raw_input())]
   plotter = getattr(plotters, plt_name)(serial_port)
   return plotter
