from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.utils.geometry import *

class Rectangle(_CompoundHPGL):
   '''Compound Rectangle. Can be rotated. Cannot be filled'''

   _scalable = _CompoundHPGL._scalable + ['width', 'height']

   def __init__(self, xy, width, height, rotation=0):
      _CompoundHPGL.__init__(self, xy) 
      self.width = width
      self.height = height
      self.rotation = rotation

   @property
   def _subcommands(self):
      tl = (-self.width / 2., self.height / 2.)
      tr = ( self.width / 2., self.height / 2.)
      bl = (-self.width / 2.,-self.height / 2.)
      br = ( self.width / 2.,-self.height / 2.)

      tl = rotate2d(tl, self.rotation)
      tr = rotate2d(tr, self.rotation)
      bl = rotate2d(bl, self.rotation)
      br = rotate2d(br, self.rotation)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append( PU( ) )
      result.append( PA((self.xabsolute + tl[0], self.yabsolute + tl[1])) )
      result.append( PD() )
      result.append( PA((self.xabsolute + tr[0], self.yabsolute + tr[1])) )
      result.append( PA((self.xabsolute + br[0], self.yabsolute + br[1])) )
      result.append( PA((self.xabsolute + bl[0], self.yabsolute + bl[1])) )
      result.append( PA((self.xabsolute + tl[0], self.yabsolute + tl[1])) )
      result.append( PU() )
      return result

