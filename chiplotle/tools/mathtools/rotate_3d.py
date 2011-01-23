import math


def rotate_3d(xyz, xyzrot):
   '''3D rotation. 

   - `xyz` is a triple (x, y, z) of coordinates.
   - `xyzrot` is a triple (xr, yr, zr) of angles of roation.
   '''
   if not len(xyz) == 3:
      raise ValueError('Coordinate tuple `xyz` is not a triple.')
   if not len(xyzrot) == 3:
      raise ValueError('Rotation tuple `xyzrot` is not a triple.')
   x, y, z = xyz
   ## z rotation..
   x = x * math.cos(xyzrot[2]) + y * math.sin(xyzrot[2]) 
   y = - x * math.sin(xyzrot[2]) + y * math.cos(xyzrot[2]) 
   ## y rotation..
   x = x * math.cos(xyzrot[1]) + z * math.sin(xyzrot[1]) 
   z = - x * math.sin(xyzrot[1]) + z * math.cos(xyzrot[1]) 
   ## x rotation..
   y = y * math.cos(xyzrot[0]) + z * math.sin(xyzrot[0]) 
   z = - y * math.sin(xyzrot[0]) + z * math.cos(xyzrot[0]) 
   return (x, y, z)
