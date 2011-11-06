from chiplotle import *
from chiplotle.geometry.core.layersvisitor import LayersVisitor
from chiplotle.geometry.core.layer import Layer

def test_layervisitor_01():
   '''Shapes without layer are set to layer None, the default.'''
   r = rectangle(1000, 1000)
   v = LayersVisitor()
   v.visit(r)
   assert v.layers.keys() == [None]
   assert v.layers[None] == [r]

def test_layersvisitor_02():
   '''One paths with layer gorup.'''
   r1 = rectangle(1000, 1000)
   l = Layer([r1], 1)
   v = LayersVisitor()
   v.visit(l)
   assert v.layers.keys() == [1]
   assert v.layers[1] == [r1]

def test_layersvisitor_03():
   '''Nested Layers work as expected.'''
   r1 = rectangle(1000, 1000)
   r2 = rectangle(500, 500)
   t3 = isosceles(500, 200)

   l1 = Layer([r1], 1)
   l2 = Layer([l1, r2], 2)
   l3  = Layer([t3, l2], 3)

   v = LayersVisitor()
   v.visit(l3)

   assert v.layers.keys() == [1, 2, 3]
   assert v.layers[1] == [r1]
   assert v.layers[2] == [r2]
   assert v.layers[3] == [t3]

#   r1   r2   t3
#   .     .   .
#   l1   .   .
#    .  .   .
#     l2   .
#      .  .
#       l3

def test_layersvisitor_04():
   '''Nested Layers and Groups work as expected.'''
   r1 = rectangle(1000, 1000)
   r2 = rectangle(500, 500)
   t3 = isosceles(500, 200)

   l1 = Layer([r1], 1)
   g1 = group([l1, r2])
   l3 = Layer([t3, g1], 3)

   v = LayersVisitor()
   v.visit(l3)

   assert v.layers.keys() == [1, 3]
   assert v.layers[1] == [r1]
   assert v.layers[3] == [t3, r2]

#   r1   t3   r3
#   .     .   .
#   l1   .   .
#    .  .   .
#     g1   .
#      .  .
#       l3

def test_layervisitor_05():
   '''Multiple nestings work as expected.'''
   c1, c2, c3 = [circle(1000 * i) for i in range(1, 4)]
   r = rectangle(1000, 1000)
   t = isosceles(1000, 2000)

   l_leaf = Layer([c1], 'leaf')
   g1 = Group([l_leaf, c2, c3])
   l_bottom = Layer([g1], 'bottom')

   l_med = Layer([l_bottom, r], 'med')
   
   l_top = Layer([l_med, t], 'top')
   
   v = LayersVisitor()
   v.visit(l_top)

   assert sorted(v.layers.keys()) == ['bottom', 'leaf', 'med', 'top']
   assert v.layers['top']     == [t]
   assert v.layers['med']     == [r]
   assert v.layers['bottom']  == [c2, c3]
   assert v.layers['leaf']    == [c1]

#   c1   c2 c3  r  t
#   .     . .   .  .
#   l_l  . .    .  .
#     . . .    .  .
#       g1    .  .
#       .    .  .
#      l_b  .  .
#        . .  .
#        l_m .
#         . .
#         l_t

## DEPRECATED ##
############################################################

#from chiplotle.geometry.core.layersvisitor import LayersVisitor
#
#def test_layersvisitor_01():
#   '''Simple paths with set layer.'''
#   r1 = rectangle(1000, 1000)
#   r1.layer = 1
#   v = LayersVisitor()
#   v.visit(r1)
#   assert v.layers.keys() == [1]
#   assert v.layers[1] == [r1]
#
#
#def test_layervisitor_01b():
#   '''Shapes without layer are set to layer None, the default.'''
#   r = rectangle(1000, 1000)
#   v = LayersVisitor()
#   v.visit(r)
#   assert v.layers[None] == [r]
#   assert v.layers.keys() == [None]
#
#
#def test_layersvisitor_02():
#   '''A group defines the layer of it's undelying Shapes, 
#   if the layer of these underlying shapes is set to None.
#   Shapes with their layer set override the Group layer.'''
#   r1 = rectangle(1000, 1000)
#   r1.layer = 1
#   r2 = rectangle(500, 500)
#   r2.layer = None
#
#   g = Group([r1, r2])
#   g.layer = 2
#
#   v = LayersVisitor()
#   v.visit(g)
#
#   assert v.layers.keys() == [1, 2]
#   assert v.layers[1] == [r1]
#   assert v.layers[2] == [r2]
#
#
#   
#def test_layersvisitor_03():
#   '''Nested Groups work as expected.'''
#   r1 = rectangle(1000, 1000)
#   r1.layer = 1
#   r2 = rectangle(500, 500)
#   r2.layer = None
#   t  = isosceles(500, 200)
#   t.layer = None
#
#   rg = Group([r1, r2])
#   rg.layer = 2
#   g = Group([t, rg])
#   g.layer = 3
#
#   v = LayersVisitor()
#   v.visit(g)
#
#   assert v.layers[1] == [r1]
#   assert v.layers[2] == [r2]
#   assert v.layers[3] == [t]
#
#
#def test_layervisitor_04():
#   '''Multiple nestings work as expected.'''
#   circs = [circle(1000 * i) for i in range(1, 3)]
#   circs[0].layer = 'leaf'
#   gcircs = Group(circs)
#   gcircs.layer = 'bottom'
#
#   r = rectangle(1000, 1000)
#   med = Group([gcircs, r])
#   med.layer = 'med'
#   
#   t = isosceles(1000, 2000)
#   top = Group([med, t])
#   top.layer = 'top'
#   
#   v = LayersVisitor()
#   v.visit(top)
#
#   assert set(v.layers.keys()) == set(['bottom', 'med', 'top', 'leaf'])
#   assert v.layers['top']     == [t]
#   assert v.layers['med']     == [r]
#   assert v.layers['bottom']  == circs[1:]
#   assert v.layers['leaf']    == circs[0:1]
