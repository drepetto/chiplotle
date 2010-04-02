from chiplotle.utils.imports.package_import import _package_import

_package_import(__path__[0], globals( ))

#from chiplotle.hpgl.compound import histograms
from chiplotle.hpgl.compound.histograms import *

## remove unnecessary modules...
globals().pop('histograms')
