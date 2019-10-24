from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.core.interfaces.interface import _Interface
from chiplotle.plotters.margins.marginssoft import MarginsSoft
from chiplotle.plotters.margins.marginshard import MarginsHard


class MarginsInterface(_Interface):
    def __init__(self, client):
        _Interface.__init__(self, client)
        self._soft = MarginsSoft(client)
        self._hard = None
        ## check if hard margin (OH) is supported by plotter...
        if b"OH" in client.allowedHPGLCommands:
            self._hard = MarginsHard(client)

    @property
    def soft(self):
        """Read-only reference to MarginsSoft."""
        return self._soft

    @property
    def hard(self):
        """Read-only reference to MarginsHard."""
        return self._hard
