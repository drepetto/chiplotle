from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.plotters.hp7576a import HP7576A

class HP7575A(HP7576A):
    def __init__(self, ser, **kwargs):
        HP7576A.__init__(self, ser, **kwargs)
        self.type = "HP7575A"

