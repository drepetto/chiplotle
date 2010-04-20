import os

def _run_chiplotle( ):
   '''The function runs Python, imports Chiplotle and initializes 
   a plotter.
   '''
   python_code = [ ]
   python_code.append("print ' '")
   python_code.append("print ' +--------------+'")
   python_code.append("print ' |  Chiplotle!  |'")
   python_code.append("print ' +--------------+'")
   python_code.append("import sys")
   python_code.append("sys.ps1 = 'chiplotle> '")
   python_code.append("del sys")
   python_code.append("from chiplotle import *")
   #python_code.append("plotter = instantiate_plotter( )")
   python_code.append("plts = instantiate_plotters( )")
   python_code.append("if plts: plotter = plts[0]")

   os.system('''python -i -c "%s"''' % '\n'.join(python_code))

