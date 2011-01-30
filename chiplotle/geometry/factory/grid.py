from chiplotle.geometry.shapes.path import Path
from chiplotle.geometry.shapes.group import Group

def grid(width, height, width_divisions,height_divisions):
   '''Rectangular grid. 

   - `width` : ``int`` or ``float``, width of the rectangle.
   - `height` : ``int`` or ``float``, height of the rectangle.
   - `width_divisions` : ``int``, number of horizontal equidistant partitions.
   - `height_divisions` : ``int``, number of vertical equidistant partitions.
   
   '''

   ul_x = width
   bl_x = ul_x
   ur_x = ul_x + width

   ul_y = height
   ur_y = ul_y
   bl_y = ul_y - height
   
   x_step_size = width / width_divisions
   y_step_size = height / height_divisions

   g = Group()
   
   ## add horizontal lines
   for i in range(height_divisions + 1):
      horiz_points = []
      step_y = y_step_size * i
      horiz_points.append((ul_x, ul_y - step_y))
      horiz_points.append((ur_x, ur_y - step_y))
      g.append(Path(horiz_points))
   ## add vertical lines

   for i in range(width_divisions + 1):
      vert_points = []
      step_x = x_step_size * i
      vert_points.append((ul_x + step_x, ul_y))
      vert_points.append((bl_x + step_x, bl_y))
      g.append(Path(vert_points))

   return g

## RUN DEMO CODE

if __name__ == '__main__':
   from chiplotle.tools import io
   gr = grid(1000, 2000, 10, 20)
   assert isinstance(gr, Group)
   print gr.format
   io.view(gr)
