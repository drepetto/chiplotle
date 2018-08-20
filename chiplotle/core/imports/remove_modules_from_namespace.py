from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import types


def _remove_modules_from_namespace(namespace):
    for key, value in list(namespace.items( )):
        if isinstance(value, types.ModuleType) and not key.startswith('_'):
            del(namespace[key])
