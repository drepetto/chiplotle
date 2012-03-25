#!/usr/bin/env python


def compile_plotters():
   from chiplotle import plotters

   content = 'Chiplotle Known Plotters\n'
   content += '========================\n\n'

   ## get classes in plotters...
   for cls in dir(plotters):
      if not cls.startswith('__'):
         content += '.. autoclass:: chiplotle.plotters.%s\n' % cls
         content += '\t:members:\n'
         content += '\t:undoc-members:\n'
         content += '\t:show-inheritance:\n'
         ## show inherited members for generic plotter...
         if cls == 'Plotter':
            content += '\t:inherited-members:\n'
         content += '\n'


   file = open('../chapters/api/plotters.rst', 'w')

   file.write(content)
   file.close()


## TODO: change this so that the tool modules are automatically discovered.
def compile_tools():
   from chiplotle import hpgltools
   from chiplotle import io
   from chiplotle import mathtools

   content = 'Chiplotle Tools\n'
   content += '================\n\n'

   content += 'HPGL Tools\n'
   content += '-------------\n\n'
   content += _autofunction(hpgltools)

   content += 'Input-output tools\n'
   content += '---------------------\n\n'
   content += _autofunction(io)

   content += 'Math tools\n'
   content += '--------------\n\n'
   content += _autofunction(mathtools)

   file = open('../chapters/api/tools.rst', 'w')
   file.write(content)
   file.close()

def compile_geometry():
   from chiplotle.geometry import core
   from chiplotle.geometry import shapes
   from chiplotle.geometry import transforms

   content = 'Chiplotle Geometry / Shapes\n'
   content += '============================\n\n'

   content += 'Shapes\n'
   content += '--------\n\n'
   content += _autofunction(shapes)

   content += 'Transforms\n'
   content += '-------------\n\n'
   content += _autofunction(transforms)

#   content += 'Core\n'
#   content += '-------------\n\n'
#   content += _autofunction(core)

   
   file = open('../chapters/api/geometry.rst', 'w')
   file.write(content)
   file.close()


## helpers ##

def _autofunction(module):
   modulename = module.__name__
   ret = []
   for cls in dir(module):
      if not cls.startswith('_'):
         af = '.. autofunction:: %s.%s' % (modulename, cls)
         ret.append(af)
   return '\n'.join(ret) + '\n\n'


if __name__ == '__main__':
   compile_plotters()
   compile_tools()
   compile_geometry()
