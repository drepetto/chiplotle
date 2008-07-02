from chiplotle.hpgl.extended.extended import _ExtendedHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.geometry import *

class Rectangle(_ExtendedHPGL):
   '''Compound Rectangle. Can be rotated. Cannot be filled'''
   def __init__(self, x, y, width, height, rotation=0):
      _ExtendedHPGL.__init__(self, (x, y)) 
      self.width = Scalable(width)
      self.height = Scalable(height)
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

      result = _ExtendedHPGL._subcommands.fget(self)
      result.append( PU( ) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PD() )
      result.append( PA((self.x + tr[0], self.y + tr[1])) )
      result.append( PA((self.x + br[0], self.y + br[1])) )
      result.append( PA((self.x + bl[0], self.y + bl[1])) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PU() )
      return result

