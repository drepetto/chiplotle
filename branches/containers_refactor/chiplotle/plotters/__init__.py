from chiplotle.utils.imports.package_import import _package_import

_package_import(__path__[0], locals( ))

def remove_all_but_types(lst):
   '''Keep only classes.'''
   from types import TypeType
   for k, v in lst.items( ):
      if not isinstance(v, TypeType):
         del(lst[k])

remove_all_but_types(locals( ))

