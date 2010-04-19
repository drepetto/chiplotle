
def import_cleaner(locals):
   '''Keep only Classes (type Type).'''
   from types import TypeType
   for _key, _value in locals.items():
      if not isinstance(_value, TypeType) and _key != 'import_cleaner':
         del(locals[_key])

