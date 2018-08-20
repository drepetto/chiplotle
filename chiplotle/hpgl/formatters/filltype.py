from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.hpgl.commands import FT
from chiplotle.core.interfaces.formatdecorator import FormatDecorator


class FillType(FormatDecorator):

    __doc__ = FT.__doc__

    def __init__(self, filltype=None, space=None, angle=None):
        FormatDecorator.__init__(self)
        self.filltype = filltype
        self.space = space
        self.angle = angle


    @property
    def _subcommands(self):
        return [FT(self.filltype, self.space, self.angle)]
