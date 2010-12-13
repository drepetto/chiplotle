from chiplotle.hpgl.compound.hpglcompoundshape import _HPGLCompoundShape
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.tools.mathtools.rotate_2d import rotate_2d

class Rectangle(_HPGLCompoundShape):
   '''
   Compound Rectangle. Can be rotated. Cannot be filled
   
   points are returned as [[tl, tr, br, bl]]
   '''

   _scalable = _HPGLCompoundShape._scalable + ['width', 'height']

   def __init__(self, xy, width, height, rotation=0):
      _HPGLCompoundShape.__init__(self, xy) 
      self.width = width
      self.height = height
      self.rotation = rotation

      if rotation != 0:
         print "Sorry, rotation is ignored in this version!"

   @property
   def points(self):
      tl = (-self.width / 2., self.height / 2.)
      tr = ( self.width / 2., self.height / 2.)
      bl = (-self.width / 2.,-self.height / 2.)
      br = ( self.width / 2.,-self.height / 2.)

      #tl = rotate_2d(tl, self.rotation)
      #tr = rotate_2d(tr, self.rotation)
      #bl = rotate_2d(bl, self.rotation)
      #br = rotate_2d(br, self.rotation)     
      
      return [[tl, tr, br, bl]]

   @property
   def _subcommands(self):

      the_points = self.points[0]
      tl = the_points[0]
      tr = the_points[1]
      br = the_points[2]
      bl = the_points[3]
      
      result = _HPGLCompoundShape._subcommands.fget(self)
      result.append( PU( ) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PD() )
      result.append( PA((self.x + tr[0], self.y + tr[1])) )
      result.append( PA((self.x + br[0], self.y + br[1])) )
      result.append( PA((self.x + bl[0], self.y + bl[1])) )
      result.append( PA((self.x + tl[0], self.y + tl[1])) )
      result.append( PU() )
      return result

