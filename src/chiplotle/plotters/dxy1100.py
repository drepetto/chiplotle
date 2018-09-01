from chiplotle.plotters import DXY1300


class DXY1100(DXY1300):
    def __init__(self, ser, **kwargs):
        super(self, DXY1100).__init__(ser, **kwargs)
        self.type = "DXY-1100"
