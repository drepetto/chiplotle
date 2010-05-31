from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive
from chiplotle.hpgl.abstract.positional import _Positional
from chiplotle.hpgl.commands import PU, PD, PA, PR 
import copy
from numpy import concatenate

def fuse_consecutive_pen_commands(data):
   '''Fuse consecutive PU, PD, PA, PR commands. 
   i.e., [PU(1, 2), PD(3, 4), PD(5, 6), PD(7, 8), PU(9, 10)]
         -->
         [PU(1, 2), PD(3, 4, 5, 6, 7, 8), PU(9, 10)]
   Returns a fresh copy of all the commands.
   '''
   assert isinstance(data, list)
   data = copy.deepcopy(data)
   result = [ ]
   prev = data[0]
   for curr in data[1:]:
      if isinstance(curr, (PU, PD, PA, PR)) and (type(curr) == type(prev)):
            prev.xy = concatenate((prev.xy, curr.xy))
      else: 
         result.append(prev)
         prev = curr
   return result

def split_long_pen_commands(data):
   '''Opposite of fuse. 
    i.e.,[PU(1, 2), PD(3, 4, 5, 6, 7, 8), PU(9, 10)]
         -->
         [PU(1, 2), PD(3, 4), PD(5, 6), PD(7, 8), PU(9, 10)]
   Returns a fresh copy of all the commands.
   '''
   assert isinstance(data, list)
   result = [ ]
   for com in data:
      if isinstance(com, (PU, PD, PA, PR)):
#         xs = list(com.xy[0::2])
#         ys = list(com.xy[1::2])
         xs = list(com.x)
         ys = list(com.x)
         result.extend([eval('%s((%s,%s))' % \
            (com._name,x,y)) for x, y in zip(xs, ys)])
      else: 
         result.append(com)
   return result

def remove_redundant_pens(data):
   '''Removes redundant PU, PD. e.g. [PU(), PA(1,2), PU(), PA(4,4)].
   PUs and PDs are only removed in they have no coordinate values 
   (i.e. they don't draw).
   This method does not return and acts on the input data.'''
   memory = None
   for com in data[:]:
      if isinstance(com, (PU, PD)) and len(com.xy) == 0:
         if type(com) == type(memory):
            data.remove(com)
         else:
            memory = com
   
