#!/usr/bin/env python

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


file = open('../chapters/api/chiplotle_compound.rst', 'w')

file.write(content)
file.close( )
