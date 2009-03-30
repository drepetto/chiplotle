from chiplotle.plotters.drawingplotter import _DrawingPlotter

class Plotter(_DrawingPlotter):
    def __init__(self, ser, **kwargs):
        _DrawingPlotter.__init__(self, ser, **kwargs)
        self.type = "Generic"

