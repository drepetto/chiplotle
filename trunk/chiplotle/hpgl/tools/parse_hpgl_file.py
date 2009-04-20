import re

def parse_hpgl_file(filename):
   _knownUnsupportedCommands = ('PW','PC')
   f = open(filename)
   fs = f.read()
   f.close()
   fs = fs.replace('\n',';')
   #commands = fs.split(';')
   commands = re.split(';+', fs)
   #print commands
   result = []
   for c in commands:
      #print c
      head = c[0:2]
      ### REMOVE KNOWN INVALID COMMANDS ###
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
         print '*** ERROR: Could not create %s(%s)' % (head, body)
   return result
