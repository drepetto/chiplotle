#! /usr/bin/env python
from chiplotle.cfg.cfg import CHIPLOTLE_DIR
from chiplotle.hpgl import commands
#from chiplotle.documentation.templates.html import *
import os

output_file_path = os.sep.join([CHIPLOTLE_DIR, 'documentation', 'chapters', 'hpgl_classes', 'text.html'])

commands_output_file = open(output_file_path, 'w')

contents = [ ]
classes = dir(commands)
for name in classes:
   if not name.startswith('_'):
      doc = eval('commands.%s.__doc__' % name)
      if doc:
         doc = doc.split('\n')
         doc = '<br>'.join(doc[1:])
         text = '<h3>%s</h3><p>%s</p>' % (name, doc) 
         contents.append(text)

title = '<h1>HPGL Classes</h1>'
contents.insert(0, title)
contents_str = '\n'.join(contents)
commands_output_file.write(contents_str)
commands_output_file.close( )
