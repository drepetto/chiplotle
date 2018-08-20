from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from chiplotle.core.visitor import Visitor


class TagsVisitor(Visitor):
    '''Sort / group shapes by tags.'''

    def __init__(self):
        self.tags = {}

    def visit_Group(self, node, *args, **kwargs):
        self._sort_by_tag(node)
        for s in node:
            self.visit(s, *args, **kwargs)

    def visit__Shape(self, node, *args, **kwargs):
        self._sort_by_tag(node)


    ## private ##

    def _sort_by_tag(self, shape):
        for tag in shape.meta.tags:
            if tag in self.tags:
                self.tags[tag].append(shape)
            else:
                self.tags[tag] = [shape]

