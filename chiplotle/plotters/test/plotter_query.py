from chiplotle import *
from chiplotle.utils.plottertools import instantiate_plotters

plotter = instantiate_plotters( )[0]

assert plotter._buffer_space
assert plotter.id
assert plotter.actual_position
assert plotter.commanded_position
assert plotter.digitized_point
assert plotter.output_error
assert plotter.options
assert plotter.output_P1P2
assert plotter.status
