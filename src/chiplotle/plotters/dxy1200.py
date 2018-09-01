from chiplotle.plotters.dxy1300 import DXY1300


class DXY1200(DXY1300):
    def __init__(self, ser, **kwargs):
        super(DXY1200, self).__init__(ser, **kwargs)
        self.type = "DXY-1200"
