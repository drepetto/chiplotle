from chiplotle import *
from chiplotle.tools.plottertools import instantiate_plotters

plotter = instantiate_plotters( )[0]

assert plotter._buffer_space
assert plotter.id
assert plotter.actual_position
assert plotter.commanded_position
assert plotter.digitized_point
assert plotter.output_error
assert plotter.options
assert plotter.output_p1p2
assert plotter.status
