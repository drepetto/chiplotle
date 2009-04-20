from chiplotle.hpgl import commands as hpgl
import re

def import_hpgl_file(filename):
   _knownUnsupportedCommands = ('PW','PC')
   f = open(filename)
   fs = f.read()
   f.close()
   fs = fs.replace('\n',';')
   comms = re.split(';+', fs)
   result = []
   for c in comms:
      if c: ## not an empty string: ''
         head = c[0:2]
         if head in _knownUnsupportedCommands:
            continue
         if head in ('PU','PD','PA','PR', 'RA','RR', 'ER','EA'):
            body = '(%s)' % c[2:]
         elif head in ('AR', 'AA'):
            body = '(%s),%s' % (c[2:4], c[4:])
         else:
            body = c[2:]
         try:
            cout = eval('hpgl.%s(%s)' % (head, body))
            result.append(cout)
         except:
            print 'WARNING: Could not create %s(%s)' % (head, body)
   return result
