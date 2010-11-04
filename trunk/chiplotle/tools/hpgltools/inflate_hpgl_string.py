from chiplotle.hpgl import commands as hpgl
from chiplotle.tools.hpgltools.parse_hpgl_string import parse_hpgl_string
from chiplotle.tools.logtools.apply_logger import apply_logger
#from chiplotle.tools.logtools.get_logger import get_logger

@apply_logger
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
   ## TODO delete this.
   #logger = get_logger('inflate_hpgl_string')

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
         if head in ('PU','PD','PA','PR', 'RA','RR','ER','EA','IP','IW','SC'):
            body = '(%s)' % c[2:]
         elif head in ('AR', 'AA'):
            parameters = c[2:].split(',')
            x = parameters.pop(0)
            y = parameters.pop(0)
            body = '(%s,%s),%s' % (x, y, ','.join(parameters))
         else:
            body = c[2:]
         try:
            cout = eval('hpgl.%s(%s)' % (head, body))
            result.append(cout)
         except:
            msg = 'Could not create %s(%s)...' % (head, body)
            msg += ' The command is either malformed or unrecognized.'
            inflate_hpgl_string.logger.warning(msg)
   return result
