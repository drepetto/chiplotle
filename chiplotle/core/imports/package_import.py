from chiplotle.core.imports.get_functions_in_module \
   import _get_functions_in_module
from chiplotle.core.imports.remove_modules_from_namespace \
   import _remove_modules_from_namespace
import os

def _package_import(path, namespace):
   '''Non-recursive import helper. 
   All the functions and classes inside modules (leaf-modules, *.py files) 
   found in `path` are imported into `namespace`.'''
   module = path[path.rindex('chiplotle'):]
   module = module.replace(os.sep, '.')

   for element in os.listdir(path):
      if os.path.isfile(os.path.join(path, element)):
         if not element.startswith('_') and element.endswith('.py'):
            ## import function inside module
            submod = os.path.join(module, element[:-3])
            functions = _get_functions_in_module(submod)
            for f in functions:
               namespace[f.__name__] = f

   ## remove modules
   _remove_modules_from_namespace(namespace)
   ## remove myself
   del(namespace['_package_import'])
