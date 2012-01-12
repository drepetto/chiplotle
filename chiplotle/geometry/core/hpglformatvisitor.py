from chiplotle.core.visitor import Visitor
from chiplotle.tools.hpgltools import convert_coordinates_to_hpgl_absolute_path
import chiplotle.hpgl.commands as hpgl
import copy

class HPGLFormatVisitor(Visitor):
   '''Visitor that collects shapes and returns their HPGL representation.'''
   
   def __init__(self):
      self.hpgl = []


   def visit_Group(self, node, formatters=None):
      frmtrs = self._update_formatters(node, formatters)
      for s in node:
         self.visit(s, frmtrs)


   def visit_Polygon(self, node, formatters=None):
      frmtrs = self._update_formatters(node, formatters)
      result = self._formatters_to_hpgl(frmtrs)
      result += self._polygon_to_hpgl(node)
      self.hpgl += result
      

   def visit_Path(self, node, formatters=None):
      frmtrs = self._update_formatters(node, formatters)
      result = self._formatters_to_hpgl(frmtrs)
      result += self._path_to_hpgl(node)
      self.hpgl += result
      

   def visit_Label(self, node, formatters=None):
      frmtrs = self._update_formatters(node, formatters)
      result = self._formatters_to_hpgl(frmtrs)
      result += self._label_to_hpgl(node)
      self.hpgl += result


   ## properties ##

   @property
   def format(self):
      return ''.join([c.format for c in self.hpgl])


   ## private methods ##
   
   def _update_formatters(self, node, formatters):
      result = formatters.copy() if formatters is not None else {}
      for fd in node.formatters:
         result[fd.__class__.__name__] = fd
      return result 


   def _path_to_hpgl(self, path):
      return convert_coordinates_to_hpgl_absolute_path(path._preformat_points)


   def _polygon_to_hpgl(self, poly):
      path = convert_coordinates_to_hpgl_absolute_path(poly._preformat_points)
      result = path[0:2] + [hpgl.PM(0)] + path[2:] + [hpgl.PM(2), hpgl.EP()]
      if poly.filled:
         result.append(hpgl.FP())
      return result


   def _label_to_hpgl(self, label):
      from chiplotle.hpgl.label import Label
      from chiplotle.tools.mathtools import polar_to_xy
      import math
      angle = label.angle
      if label.never_upside_down:
         if math.pi * 3 / 2.0 > angle > math.pi / 2.0:
            angle += math.pi

      origin    = label.HPGL_ORIGIN_MAP[label.origin]
      hpgllabel =  Label(text        = label.text,
                           charwidth   = label.charwidth,
                           charheight  = label.charheight,
                           charspace   = label.charspace,
                           linespace   = label.linespace,
                           origin      = origin,
                           direction   = polar_to_xy((1, angle))
                           )
      return [hpgl.PA([label.points[0]]), hpgllabel]


   def _formatters_to_hpgl(self, formatters):
      result = []
      for f in formatters.values():
         result += f._subcommands
      return result
   
