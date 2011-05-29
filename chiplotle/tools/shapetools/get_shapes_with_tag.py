from chiplotle.geometry.core.tagsvisitor import TagsVisitor

def get_shapes_with_tag(shape, tag):
   '''Returns all the shapes with the given tag.'''
   v = TagsVisitor()
   v.visit(shape)
   return v.tags.get(tag) or []



if __name__ == '__main__':
   from chiplotle import *

   c1 = circle(1000)
   c1.meta.tags.update(['circle', 'red'])

   c2 = circle(2000)
   c2.meta.tags.update(['circle', 'blue'])

   r1 = rectangle(100, 1000)
   r1.meta.tags.update(['rect', 'blue'])

   t1 = isosceles(100, 1000)
   t1.meta.tags.add('triangle')

   g = Group([c1, c2, r1, t1])
   circles  = get_shapes_with_tag(g, 'circle')
   reds     = get_shapes_with_tag(g, 'red')
   blues    = get_shapes_with_tag(g, 'blue')
   triang   = get_shapes_with_tag(g, 'triangle')
   assert circles == [c1, c2]
   assert reds    == [c1]
   assert blues   == [c2, r1]
   assert triang  == [t1]
