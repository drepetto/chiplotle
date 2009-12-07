from chiplotle.utils.imports.package_import import _package_import

_package_import(__path__[0], globals( ))

#from chiplotle.utils.imports.import_functions_in_package_to_namespace import _import_functions_in_package_to_namespace

#_import_functions_in_package_to_namespace(__path__[0], globals( ))



## TODO: delete this. The above call replaces this.
#from os import listdir
#from chiplotle.utils.import_cleaner import import_cleaner
#
#_fns = listdir(__path__[0])
#_modules = [_fn[:-3] for _fn in _fns
#   if _fn.endswith('.py') and not _fn.startswith('_')]
#
#for _module in sorted(_modules):
#   exec('from %s import *' % _module)
#
#import_cleaner(locals())
#del import_cleaner

