from chiplotle.core.visitor import Visitor

class TransformVisitor(Visitor):
   '''"Crawler" pattern encapsulation for transformations applied to _Shapes.
   Separates the "what it does" (action) from "how it does it" (traversal).'''   
   def __init__(self, transform):
      self.transform = transform


   def visit_Group(self, node, *args, **kwargs):
      for s in node:
         self.visit(s, *args, **kwargs)


   def visit_TransformLock(self, node, *args, **kwargs):
      if self.transform.func_name in node.lock_transforms:
         self._handle_transform_map(node, *args, **kwargs)
      else:
         for s in node:
            self.visit(s, *args, **kwargs)


   def visit__Shape(self, node, *args, **kwargs):
      node.points = self.transform(node.points, *args, **kwargs)


   ## private ##

   def _handle_transform_map(self, node, *args, **kwargs):
      tmp = self.transform
      t, p = node.get_transform(self.transform)(node.points, *args, **kwargs)
      self.transform = t
      for s in node:
         self.visit(s, *p)
      self.transform = tmp
