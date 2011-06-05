from chiplotle.core.visitor import Visitor


class AffixFormatVisitor(Visitor):
   '''Hard-sets formatters defined in Groups onto the drawable _Shapes.
      This cannot be undone!
      Useful as an operation previous to splitting a shape tree to avoid
      loosing the implied formating information across groups.
   '''

   def visit_Group(self, node, formatters=None):
      formatters = self._update_formatters(node, formatters)
      for s in node:
         self.visit(s, formatters)


   def visit__Shape(self, node, formatters=None):
      frmtrs = self._update_formatters(node, formatters)
      node.formatters = frmtrs.values()
      


   ## private methods ##
   
   def _update_formatters(self, node, formatters):
      result = formatters.copy() if formatters is not None else {}
      for fd in node.formatters:
         result[fd.__class__.__name__] = fd
      return result 


