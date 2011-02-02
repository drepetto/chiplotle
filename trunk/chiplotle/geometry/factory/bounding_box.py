from chiplotle.geometry.factory.rectangle import rectangle
from chiplotle.geometry.destructive_transforms.offset import offset
from chiplotle.tools.geometrytools.get_bounding_coordinate_pairs \
   import get_bounding_coordinate_pairs

def bounding_box(shape):
   '''Return a bounding box shape (rectangle) enclosing the givne `shape`.'''

   ll, ur = get_bounding_coordinate_pairs(shape)

   w, h = ur - ll
   center_x = ll.x + w / 2.0
   center_y = ll.y + h / 2.0
   
   r =  rectangle(w, h)
   offset(r, (center_x, center_y))
   return r



## DEMO CODE ##
if __name__ == '__main__':
   from chiplotle.geometry.factory.circle import circle
   from chiplotle.geometry.destructive_transforms.noise import noise
   from chiplotle.geometry.shapes.group import Group
   from chiplotle.tools import io

   c = circle(1000)
   offset(c, (100, 500))
   noise(c, 500)
   bb = bounding_box(c)
   
   io.view(Group([bb, c]))

