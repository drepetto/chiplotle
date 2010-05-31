from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.utils.geometry import *

class Cube(_CompoundHPGL):
   '''A 3D Cube. Can be rotated on x, y, and z.'''

   _scalable = ['width', 'height', 'depth']

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
      blh = rotate3d(blh, self.rotation)[0:2]
      brh = rotate3d(brh, self.rotation)[0:2]
      tlh = rotate3d(tlh, self.rotation)[0:2]
      trh = rotate3d(trh, self.rotation)[0:2]
      bll = rotate3d(bll, self.rotation)[0:2]
      brl = rotate3d(brl, self.rotation)[0:2]
      tll = rotate3d(tll, self.rotation)[0:2]
      trl = rotate3d(trl, self.rotation)[0:2]

      result = _CompoundHPGL._subcommands.fget(self)
      result.append(PA( ))
      ## high square...
      result.append(PU(self.xyabsolute + blh))
      result.append(PD(self.xyabsolute + brh))
      result.append(PD(self.xyabsolute + trh))
      result.append(PD(self.xyabsolute + tlh))
      result.append(PD(self.xyabsolute + blh))
      ## low square...
      result.append(PU(self.xyabsolute + bll))
      result.append(PD(self.xyabsolute + brl))
      result.append(PD(self.xyabsolute + trl))
      result.append(PD(self.xyabsolute + tll))
      result.append(PD(self.xyabsolute + bll))
      ## connect squares...
      result.append(PU(self.xyabsolute + blh))
      result.append(PD(self.xyabsolute + bll))
      result.append(PU(self.xyabsolute + brh))
      result.append(PD(self.xyabsolute + brl))
      result.append(PU(self.xyabsolute + tlh))
      result.append(PD(self.xyabsolute + tll))
      result.append(PU(self.xyabsolute + trh))
      result.append(PD(self.xyabsolute + trl))
      result.append(PU( ))
      return result

