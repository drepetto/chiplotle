from chiplotle.hpgl.abstract.hpglcommand import _HPGLCommand
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.extended.container import Container
from chiplotle.hpgl.utils import *
from chiplotle.hpgl.scalable import Scalable
import chiplotle.hpgl.commands as hpgl
import re

def _scale_command(arg, val):
   attrs = arg.__dict__.keys()
   for an in attrs:
      a = getattr(arg, an)
      if isinstance(a, Scalable):
         a *= val

def scale(arg, val):
   if isinstance(arg, Container):
      _scale_command(arg, val)
      for c in arg:
         _scale_command(c, val)
   elif isinstance(arg, _HPGLCommand):
      _scale_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _scale_command(c, val)

def _transpose_command(arg, val):
#   if hasattr(arg, '_xy'):
   if isinstance(arg, _Positional) and arg._transposable:
      arg._xy[0::2] += val[0]
      arg._xy[1::2] += val[1]

def transpose(arg, val):
   if isinstance(arg, _HPGLCommand):
      _transpose_command(arg, val)
   elif isinstance(arg, (list, tuple)):
      for c in arg:
         _transpose_command(c, val)


def parse_hpgl_file(filename):
   _knownUnsupportedCommands = ('PW','PC')
   f = open(filename)
   fs = f.read()
   f.close()
   fs = fs.replace('\n',';')
   fs = fs.replace('\r',';')
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
         print 'Command skipped. File created anyway. '
   return result

def relativize(data):
   '''Convert all absolute positions in to relative positions.
   WARNING! this currently ONLY works on PU, PD, PA!.'''
   result = [ ]
   data = split_long_pen_commands(data)
   prev = data[0]
   for curr in data[1:]:
      if isinstance(prev, (PU, PD, PA)) and isinstance(curr, (PU, PD, PA)):
         diff = curr.xy - prev.xy
         if isinstance(curr, (PU, PD)):
            result.append(eval('%s()' % curr._name))
         result.append(PR(diff))
         prev = curr
   remove_redundant_pens(result)
   return result
