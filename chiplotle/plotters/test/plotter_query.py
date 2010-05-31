from chiplotle import *
from chiplotle.utils.plottertools import instantiate_plotters

plotter = instantiate_plotters( )[0]

assert plotter._buffer_space
assert plotter.id
assert plotter.actual_position
assert plotter.commandedPosition
assert plotter.digitizedPoint
assert plotter.outputError
#assert plotter.hardClipLimits
assert plotter.options
assert plotter.outputP1P2
assert plotter.status
#assert plotter.window

