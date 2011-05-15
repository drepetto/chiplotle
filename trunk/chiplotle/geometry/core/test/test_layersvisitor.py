from chiplotle import *
from chiplotle.geometry.core.layersvisitor import LayersVisitor

def test_layersvisitor_01():
   '''Simple paths.'''
   r1 = rectangle(1000, 1000)
   r1.layer = 1
   r2 = rectangle(500, 500)
   r2.layer = None

   v = LayersVisitor()
   v.visit(r1)

   assert v.layers.keys() == [1]
   assert v.layers[1] == [r1]

   v.visit(r2)

   assert v.layers[None] == [r2]


def test_layersvisitor_02():
   '''A group defines the layer of it's undelying Shapes, 
   if the layer of thesee these underlying shapes is set to None.
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
   '''Shapes without layer are set to layer None, the default.'''
   r = rectangle(1000, 1000)

   v = LayersVisitor()
   v.visit(r)

   assert v.layers[None] == [r]
   assert v.layers.keys() == [None]
