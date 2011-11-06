from chiplotle.geometry.core.layersvisitor import LayersVisitor
from chiplotle.geometry.core.affixformatvisitor import AffixFormatVisitor
import copy

def interactive_plot_layers(shape, plotter):
   '''Sorts given `shape` by layers and interactively plots,
   requesting the use to change page every time a layer is done printing.'''
   shape = copy.deepcopy(shape)
   v = AffixFormatVisitor()
   v.visit(shape)
   v = LayersVisitor()
   v.visit(shape)
   print 'Layers collected: ', v.layers.keys()

   for layer in sorted(v.layers.keys()):
      print 'Please set/change paper for layer [%s].' % layer
      reply = raw_input('Hit ENTER to plot layer, "n" to skip:')
      if reply.lower( ) == 'n':
         continue
      print 'Plotting layer [%s]...' % layer
      plotter.write(v.layers[layer])
      print 'Done plotting layer [%s].' % layer



if __name__ == '__main__':
   from chiplotle import *

   r1 = rectangle(1000, 1000)
   r1.layer = 1
   r2 = rectangle(500, 500)
   r2.layer = None
   t  = isosceles(500, 200)
   t.layer = None

   rg = Group([r1, r2])
   rg.layer = 2
   g = Group([t, rg])
   g.layer = 3

   plotter = instantiate_plotters()[0]
   interactive_plot_layers(g, plotter)
