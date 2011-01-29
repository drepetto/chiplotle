from chiplotle.core.cfg.cfg import __version__
import os

def _run_chiplotle( ):
   '''The function runs Python, imports Chiplotle and initializes 
   a plotter.
   '''
   python_code = [ ]
   python_code.append("print ' '")
   python_code.append("print '  +-----------------------+'")
   python_code.append("print '  |   Chiplotle! v.%s  |'" % __version__)
   python_code.append("print '  +-----------------------+'")
   python_code.append("print ' '")
   python_code.append("import sys")
   python_code.append("sys.ps1 = 'chiplotle> '")
   python_code.append("del sys")
   python_code.append("from chiplotle import *")
   python_code.append("plts = instantiate_plotters( )")
   python_code.append("plotter = plts[0]")

   ##                                 '\n' does now work on Windowz!
   os.system('''python -i -c "%s"''' % ';'.join(python_code))

