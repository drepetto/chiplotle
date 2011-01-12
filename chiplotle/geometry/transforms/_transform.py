
class _Transform(object):
   
   ## PUBLIC METHODS ##

   def transform(self, coords):
      '''Transforms the given `coords`.
      `coords` is a list of CoordinateArrays'''
      ## This must be implemented by all subclasses of _Transform.


   ## OVERRIDES ##

   def __call__(self, shape):
      shape.transforms.append(self)

