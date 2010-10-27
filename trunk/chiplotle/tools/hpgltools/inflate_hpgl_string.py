from chiplotle.hpgl import commands as hpgl
from chiplotle.tools.hpgltools.parse_hpgl_string import parse_hpgl_string
#import re

def inflate_hpgl_string(string, filter_commands=None):
   '''Reads a text string and "inflates" it by creating
   Chiplotle-HPGL class instances of the found HPGL commands.

   Example::

      chiplotle> square = inflate_hpgl_string('SP1;')
      chiplotle> square
      [SP(1)]

   Example::

      chiplotle> square = inflate_hpgl_string('IN;SP1;PA10,10;', ['IN'])
      chiplotle> square
      [SP(1), PA((10, 10))]
   '''
   filter_commands = filter_commands or [ ]

   if not isinstance(string, type('abc')):
      raise TypeError('`string` must be a string')
   if not isinstance(filter_commands, list):
      msg = '`filter_commands` must be a list of string HPGL commands.'
      raise TypeError(msg)

   _unsupported_commands = ('PW','PC', 'LA', 'WU', 'BP')
   #string = string.replace('\n',';')
   #comms = re.split(';+', string)
   comms = parse_hpgl_string(string)
   result = []
   for c in comms:
      if c: ## not an empty string: ''
         head = c[0:2]
         if head in filter_commands:
            continue
         if head in _unsupported_commands:
            continue
         if head in ('PU','PD','PA','PR', 'RA','RR', 'ER','EA',  'IP', 'SC'):
            body = '(%s)' % c[2:]
         ## TODO: this can't be right... check and reimplement.
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
