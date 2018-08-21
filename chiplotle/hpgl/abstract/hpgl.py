from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library

standard_library.install_aliases()


class _HPGL(object):

    ## a list of attributes that can be scaled.
    _scalable = []

    @property
    def _name(self):
        return self.__class__.__name__

    @property
    def format(self):
        pass

    ## OVERRIDES ##

    def __eq__(self, arg):
        if type(arg) == type(self):
            for attr in list(self.__dict__.keys()):
                if getattr(self, attr) != getattr(arg, attr):
                    return False
            return True
        else:
            return False
