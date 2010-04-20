from chiplotle import *
from chiplotle.utils.plottertools import instantiate_plotters

plotter = instantiate_plotters( )[0]

assert plotter._bufferSpace
assert plotter.id
assert plotter.actualPosition
assert plotter.commandedPosition
assert plotter.digitizedPoint
assert plotter.outputError
#assert plotter.hardClipLimits
assert plotter.options
assert plotter.outputP1P2
assert plotter.status
#assert plotter.window

