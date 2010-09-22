#!/usr/bin/env python


def compile_compound( ):
   from chiplotle.hpgl import compound

   content = 'Chiplotle Compound Commands\n'
   content += '===========================\n\n'
   #content += ':mod: `chiplotle.hpgl.compound`\n\n'

   ## get classes in compound...
   for cls in dir(compound):
      if not cls.startswith('_'):
         content += '.. autoclass:: chiplotle.hpgl.compound.%s\n' % cls
         content += '\t:members:\n'
         content += '\t:undoc-members:\n'
         content += '\t:show-inheritance:\n'
         #content += '\t:inherited-members:\n'
         content += '\n'


   file = open('../chapters/api/chiplotle_compound.rst', 'w')

   file.write(content)
   file.close( )


def compile_plotters( ):
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
   file.close( )


## TODO: change this so that the tool modules are automatically discovered.
def compile_tools( ):
   from chiplotle import hpgltools
   from chiplotle import io
   from chiplotle import mathtools

   content = 'Chiplotle Tools\n'
   content += '================\n\n'

   content += 'HPGL Tools\n'
   content += '-------------\n\n'
   for cls in dir(hpgltools):
      if not cls.startswith('_'):
         content += '.. autofunction:: chiplotle.tools.hpgltools.%s\n' % cls
         content += '\n'
   content += 'Input-output tools\n'
   content += '---------------------\n\n'
   for cls in dir(io):
      if not cls.startswith('_'):
         content += '.. autofunction:: chiplotle.tools.io.%s\n' % cls
         content += '\n'
   content += 'Math tools\n'
   content += '--------------\n\n'
   for cls in dir(mathtools):
      if not cls.startswith('_'):
         content += '.. autofunction:: chiplotle.tools.mathtools.%s\n' % cls
         content += '\n'



   file = open('../chapters/api/tools.rst', 'w')

   file.write(content)
   file.close( )


if __name__ == '__main__':
   compile_compound( )
   compile_plotters( )
   compile_tools( )
