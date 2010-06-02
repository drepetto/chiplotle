from chiplotle.hpgl import commands as hpgl
import re

def import_hpgl_file(filename):
   '''Reads a text HPGL file and "inflates" it by creating
   Chiplotle-HPGL class instances of the found HPGL commands.

   Example::

      chiplotle> square = import_hpgl_file('examples/square.hpgl')
      chiplotle> square
      [SP(pen=1), PU(xy=[ 100.  100.]), PD(xy=[ 200.  100.]), 
      PD(xy=[ 200.  200.]), PD(xy=[ 100.  200.]), 
      PD(xy=[ 100.  100.]), SP(pen=0)]
   '''

   _unsupported_commands = ('PW','PC', 'LA', 'WU', 'BP')
   f = open(filename)
   fs = f.read()
   f.close()
   fs = fs.replace('\n',';')
   comms = re.split(';+', fs)
   result = []
   for c in comms:
      if c: ## not an empty string: ''
         head = c[0:2]
         if head in _unsupported_commands:
            continue
         if head in ('PU','PD','PA','PR', 'RA','RR', 'ER','EA',  'IP', 'SC'):
            body = '(%s)' % c[2:]
         elif head in ('AR', 'AA'):
            body = '(%s),%s' % (c[2:4], c[4:])
         else:
            body = c[2:]
         try:
            cout = eval('hpgl.%s(%s)' % (head, body))
            result.append(cout)
         except:
            print 'WARNING: Could not create %s(%s)...' % (head, body)
            print '         The command is either malformed or unrecognized.'
   return result
