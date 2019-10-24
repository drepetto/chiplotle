from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.geometry.core.group import Group


class Layer(Group):
    def __init__(self, shapes, name):
        Group.__init__(self, shapes=shapes)
        self.name = name

    def __str__(self):
        return "Layer({0}, {1})".format(len(self), self.name)
