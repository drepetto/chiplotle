from chiplotle.core.visitor import Visitor

class LayersVisitor(Visitor):
   '''Sorts / splits shapes based on the layers they live in.'''
   
   def __init__(self):
      self.layers = {}

   def visit_Layer(self, node, current_layer=None, tree=''):
      for s in node:
         self.visit(s, node.name, tree=tree)

   def visit_Group(self, node, current_layer=None, tree=''):
      for s in node:
         self.visit(s, current_layer, tree)

   def visit__Shape(self, node, current_layer=None, tree=''):
      self._add_shape_to_layer(node, current_layer)
      

   ## private ##
   
   def _add_shape_to_layer(self, shape, layer):
      if self.layers.get(layer):
         self.layers[layer].append(shape)
      else:
         self.layers[layer] = [shape]

## DEPRECATED ##
################################################
#
#class LayersVisitor(Visitor):
#   '''Sorts / splits shapes based on the layers they live in.'''
#   
#   def __init__(self):
#      self.layers = {}
#
#   def visit_Group(self, node, current_layer=None):
#      if node.layer is not None:
#         current_layer = node.layer
#      for s in node:
#         self.visit(s, current_layer)
#
#   def visit__Shape(self, node, current_layer=None):
#      if node.layer is None:
#         self._add_shape_to_layer(node, current_layer)
#      else:
#         self._add_shape_to_layer(node, node.layer)
#      
#
#   ## private ##
#   
#   def _add_shape_to_layer(self, shape, layer):
#      if self.layers.get(layer):
#         self.layers[layer].append(shape)
#      else:
#         self.layers[layer] = [shape]
#
#################################################################
