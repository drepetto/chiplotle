from __future__ import division
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA, AA
from chiplotle.utils.geometry import polar2xy
import math

class Fan(_CompoundHPGL):
   '''A Fan is a slice of a donut seen from above (the hole in the middle).
   Or think of it as bent rectangle.
   
   - `xy` is the 'pole' of the radial coordinate system used to compute
      the shape.
   
   All angles are assumed to be in radians.'''
   
   _scalable = _CompoundHPGL._scalable + \
      ['radius', 'angle', 'width_angle', 'height']

   def __init__(self, xy, radius, angle, width_angle, height, chord=None, 
      filled=False, pen=None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.radius = radius
      self.angle = angle
      self.width_angle = width_angle
      self.height = height
      self.chord = chord
      self.filled = filled
      

   def _get_hpgl_fan(self):
      
      ## get corners of shape...
      ## lower_right (viewing from pole outward)
      r = self.radius - self.height / 2 ## assumes the fan is centered on (r, a)
      a = self.angle - self.width_angle / 2
      lr = polar2xy(r, a) + self.xyabsolute

      a = self.angle + self.width_angle / 2
      ll = polar2xy(r, a) + self.xyabsolute

      r = self.radius + self.height / 2 
      a = self.angle - self.width_angle / 2
      ur = polar2xy(r, a) + self.xyabsolute

      a = self.angle + self.width_angle / 2
      ul = polar2xy(r, a) + self.xyabsolute

      result = [ ]
      ## outward lines...
      result += [PU( ), PA(lr), PD( ), PA(ur)]
      result += [PU( ), PA(ll), PD( ), PA(ul)]
      ## arches...
      a = math.degrees(self.width_angle)
      result += [PU( ), PA(lr), PD( ), AA(self.xyabsolute, a)]
      result += [PU( ), PA(ur), PD( ), AA(self.xyabsolute, a)]

      return result
   
   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      ## TODO: implement FILLED...
      result += self._get_hpgl_fan( )
      return result

