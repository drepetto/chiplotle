from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools import rotate_2d

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

      tl = rotate_2d(tl, self.rotation)
      tr = rotate_2d(tr, self.rotation)
      bl = rotate_2d(bl, self.rotation)
      br = rotate_2d(br, self.rotation)

      result = _CompoundHPGL._subcommands.fget(self)
      result.append( PU( ) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PD() )
      result.append( PA((self.x + tr[0], self.y + tr[1])) )
      result.append( PA((self.x + br[0], self.y + br[1])) )
      result.append( PA((self.x + bl[0], self.y + bl[1])) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PU() )
      return result

