from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import rotate_3d

class Cube(_CompoundHPGL):
   '''A 3D Cube. Can be rotated on x, y, and z.'''

   _scalable = _CompoundHPGL._scalable + ['width', 'height', 'depth']

   def __init__(self, xy, width, height, depth, rotation=(0,0,0), pen=None):
      _CompoundHPGL.__init__(self, xy, pen) 
      self.width = width
      self.height = height
      self.depth = depth
      if not len(rotation) == 3:
         raise ValueError('`roration` must be a triple (xr, yr, zr)')
      self.rotation = rotation

   @property
   def _subcommands(self):
      blh = (-self.width / 2., -self.height / 2., self.depth / 2)
      brh = (self.width / 2., -self.height / 2., self.depth / 2)
      tlh = (-self.width / 2., self.height / 2., self.depth / 2)
      trh = (self.width / 2., self.height / 2., self.depth / 2)

      bll = (-self.width / 2., -self.height / 2., -self.depth / 2)
      brl = (self.width / 2., -self.height / 2., -self.depth / 2)
      tll = (-self.width / 2., self.height / 2., -self.depth / 2)
      trl = (self.width / 2., self.height / 2., -self.depth / 2)
      ## rotate ...
      blh = rotate_3d(blh, self.rotation)[0:2]
      brh = rotate_3d(brh, self.rotation)[0:2]
      tlh = rotate_3d(tlh, self.rotation)[0:2]
      trh = rotate_3d(trh, self.rotation)[0:2]
      bll = rotate_3d(bll, self.rotation)[0:2]
      brl = rotate_3d(brl, self.rotation)[0:2]
      tll = rotate_3d(tll, self.rotation)[0:2]
      trl = rotate_3d(trl, self.rotation)[0:2]

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PA( ))
      ## high square...
      result.append(PU(self.xy + blh))
      result.append(PD(self.xy + brh))
      result.append(PD(self.xy + trh))
      result.append(PD(self.xy + tlh))
      result.append(PD(self.xy + blh))
      ## low square...
      result.append(PU(self.xy + bll))
      result.append(PD(self.xy + brl))
      result.append(PD(self.xy + trl))
      result.append(PD(self.xy + tll))
      result.append(PD(self.xy + bll))
      ## connect squares...
      result.append(PU(self.xy + blh))
      result.append(PD(self.xy + bll))
      result.append(PU(self.xy + brh))
      result.append(PD(self.xy + brl))
      result.append(PU(self.xy + tlh))
      result.append(PD(self.xy + tll))
      result.append(PU(self.xy + trh))
      result.append(PD(self.xy + trl))
      result.append(PU( ))
      return result

