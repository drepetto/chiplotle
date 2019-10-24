from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from builtins import str
from future import standard_library

standard_library.install_aliases()


class _ChiplotleError(Exception):
    """Abstract error class for Chiplotle!"""

    ## OVERRIDES ##

    def __eq__(self, arg):
        return self.__class__.__name__ == arg.__class__.__name__

    def __repr__(self):
        return "%s( )" % self.__class__.__name__

    def __str__(self):
        return str(self.__class__.__name__)


## make Errors hashable?
#   def __hash__(self):
#      return hash(str(self))


class InitParameterError(_ChiplotleError):
    """Error returned when initialization parameter is wrong
    (e.g., wrong type, value, etc.')."""


class OperandError(_ChiplotleError):
    """Error returned when an operand in a binary or unary operation
    is wrong (e.g., wrong type, value, etc.')."""
