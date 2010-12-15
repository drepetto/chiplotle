from chiplotle.hpgl.coordinatepair import CoordinatePair
from chiplotle.hpgl.commands import PU, PD, PA

class Polygon():
   '''
      The base class for all closed shapes.
      
      A polygon, i.e. a series of points that will be connected by
      straight lines. There may be multiple closed shapes in one Polygon,
      e.g. a donut, a frame, etc.
      
      points is an [[],[],[],...] of CoordinatePairs.
      
      Each [] is considered a separate shape inside the polygon and
      will be drawn without a connection to the other []s. 
      
      offset is a CoordinatePair for moving the polygon around on the page
      
      If first_point != last_point then one final point 
      (a duplicate of the first point) will be added to close the polygon.   
   '''

   def __init__(self, points, offset):     
      self.point_lists = points
      self.offset = offset
      
      for shape in self.point_lists:
      
         first_point = shape[0]
         last_point = shape[len(shape) - 1]
      
         if first_point != last_point:
             new_last_point = CoordinatePair(first_point)
             shape.append(new_last_point)
      
   @property
   def points(self):
      return self.point_lists

   @property
   def commands(self):
      result = []
      for shape in self.points:
         result.append( PU() )
         result.append( PA(shape[0] + self.offset) )
         result.append( PD() )
         for point in shape[1:]:
            result.append( PA(point + self.offset) )
         result.append( PU() )
         
      return result

   @property
   def format(self):
      result = ''
      for c in self.commands:
         result += c.format
      return result
   
   
'''
from shapes.polygon import Polygon
sh1 = [CoordinatePair(0,0), CoordinatePair(1000,0),CoordinatePair(1000,1000),CoordinatePair(0,1000)]
sh2 = [CoordinatePair(100,100), CoordinatePair(1100,100),CoordinatePair(1100,1100),CoordinatePair(100,1100)]
poly1 = Polygon([sh1,sh2], [0,0])
poly1.points
poly1.commands
'''