from chiplotle.plotters.hp7576a import HP7576A

class HP7575A(HP7576A):
   def __init__(self, ser, **kwargs):
      HP7576A.__init__(self, ser, **kwargs)
      self.type = "HP7575A"

