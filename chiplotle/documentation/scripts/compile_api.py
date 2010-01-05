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


if __name__ == '__main__':
   compile_compound( )
   compile_plotters( )
