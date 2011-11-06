from chiplotle.geometry.core.group import Group

class Layer(Group):

   def __init__(self, shapes, name):
      Group.__init__(self, shapes = shapes)
      self.name = name

   def __str__(self):
      return 'Layer({0}, {1})'.format(len(self), self.name)
