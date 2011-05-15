from chiplotle.core.visitor import Visitor

class LayersVisitor(Visitor):
   '''Sorts / splits shapes based on the layers they live in.'''
   
   def __init__(self):
      self.layers = {}
      self.group_layer = None

   def visit_Group(self, node, *args, **kwargs):
      self.group_layer = node.layer
      for s in node:
         self.visit(s, *args, **kwargs)

   def visit__Shape(self, node, *args, **kwargs):
      if node.layer is None:
         self._add_shape_to_layer(node, self.group_layer)
      else:
         self._add_shape_to_layer(node, node.layer)
      

   ## private ##
   
   def _add_shape_to_layer(self, shape, layer):
      if self.layers.get(layer):
         self.layers[layer].append(shape)
      else:
         self.layers[layer] = [shape]

