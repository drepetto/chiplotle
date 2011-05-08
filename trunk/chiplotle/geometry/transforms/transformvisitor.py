from chiplotle.core.visitor import Visitor

class TransformVisitor(Visitor):
   '''"Crawler" pattern encapsulation for transformations applied to _Shapes.
   Separates the "what it does" (action) from "how it does it" (traversal).'''   
   def __init__(self, transform):
      self.transform = transform

   def visit_Group(self, node, *args, **kwargs):
      for s in node:
         self.visit(s, *args, **kwargs)

   def visit_Formation(self, node, *args, **kwargs):
      node.position = self.transform(node.position, *args, **kwargs)

   def visit__Shape(self, node, *args, **kwargs):
      node.points = self.transform(node.points, *args, **kwargs)

