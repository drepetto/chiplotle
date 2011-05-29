from chiplotle import *
from chiplotle.geometry.core.layersvisitor import LayersVisitor

def test_layersvisitor_01():
   '''Simple paths with set layer.'''
   r1 = rectangle(1000, 1000)
   r1.layer = 1
   v = LayersVisitor()
   v.visit(r1)
   assert v.layers.keys() == [1]
   assert v.layers[1] == [r1]


def test_layervisitor_01b():
   '''Shapes without layer are set to layer None, the default.'''
   r = rectangle(1000, 1000)
   v = LayersVisitor()
   v.visit(r)
   assert v.layers[None] == [r]
   assert v.layers.keys() == [None]


def test_layersvisitor_02():
   '''A group defines the layer of it's undelying Shapes, 
   if the layer of these underlying shapes is set to None.
   Shapes with their layer set override the Group layer.'''
   r1 = rectangle(1000, 1000)
   r1.layer = 1
   r2 = rectangle(500, 500)
   r2.layer = None

   g = Group([r1, r2])
   g.layer = 2

   v = LayersVisitor()
   v.visit(g)

   assert v.layers.keys() == [1, 2]
   assert v.layers[1] == [r1]
   assert v.layers[2] == [r2]


   
def test_layersvisitor_03():
   '''Nested Groups and Formations work as expected.'''
   r1 = rectangle(1000, 1000)
   r1.layer = 1
   r2 = rectangle(500, 500)
   r2.layer = None
   t  = isosceles(500, 200)
   t.layer = None

   rg = Group([r1, r2])
   rg.layer = 2
   g = Formation([t, rg])
   g.layer = 3

   v = LayersVisitor()
   v.visit(g)

   assert v.layers[1] == [r1]
   assert v.layers[2] == [r2]
   assert v.layers[3] == [t]


def test_layervisitor_04():
   '''Multiple nestings work as expected.'''
   circs = [circle(1000 * i) for i in range(1, 3)]
   circs[0].layer = 'leaf'
   gcircs = Group(circs)
   gcircs.layer = 'bottom'

   r = rectangle(1000, 1000)
   med = Group([gcircs, r])
   med.layer = 'med'
   
   t = isosceles(1000, 2000)
   top = Group([med, t])
   top.layer = 'top'
   
   v = LayersVisitor()
   v.visit(top)

   assert set(v.layers.keys()) == set(['bottom', 'med', 'top', 'leaf'])
   assert v.layers['top']     == [t]
   assert v.layers['med']     == [r]
   assert v.layers['bottom']  == circs[1:]
   assert v.layers['leaf']    == circs[0:1]
