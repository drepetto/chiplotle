from chiplotle.hpgl.commands import *
from chiplotle.fonts import dorkbot
from chiplotle.utils.ispair import ispair
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.compound.fancylabel import FancyLabel

class DorkbotLabel(_CompoundHPGL):
   def __init__(self, xy, text, cell_shape='square', pen=None, fill_pen=None, 
      width=None, height=None, outline_jitter=None, fill_jitter=None):
      _CompoundHPGL.__init__(self, xy, pen) 

      self.fill_pen = fill_pen
      self.font = dorkbot
      self.text = text
      self.padding = .8

      if not (ispair(outline_jitter) or (fill_jitter is None)):
         raise ValueError('outline_jitter must be (x, y) pair.')
      self.outline_jitter = outline_jitter
      if not (ispair(fill_jitter) or (fill_jitter is None)):
         raise ValueError('fill_jitter must be (x, y) pair.')
      self.fill_jitter = fill_jitter

      ## handle shape
      if cell_shape not in ('circle', 'square'):
         raise ValueError('cell_shape must be "circle" or "square".')
      self.cell_shape = cell_shape

      ## handle width and height input parameters
      if not (width or height):
         raise ValueError('At least width or height must be given.')
      self.width = width
      self.height = height
      #h = len(self.font.char_dict['a'])
      #w = len(self.font.char_dict['a'][0])
      h = 7
      w = 3
      if width and not height:
         self.height = h / w * width
      elif height and not width:
         self.width =  w / h * height


   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result += [PU( ), PA(self.xyabsolute)]

      ## outline
      if self.cell_shape == 'circle':
         cell_shape = CI(self.width / 2. / 3. * self.padding)
      else:
         cell_shape = ER((self.width / 3. * self.padding, 
            self.height / 7. * self.padding))
      outline = FancyLabel(self.xy, self.text, self.font, cell_shape, 
         self.pen, self.width, self.height, self.outline_jitter)
      result.append(outline)
      ## fill
      if self.fill_pen:
         if self.cell_shape == 'circle':
            cell_shape = WG(self.width / 2. / 3. * self.padding, 0, 359)
         else:
            cell_shape = RR((self.width / 3. * self.padding, 
               self.height / 7. * self.padding))
         fill = FancyLabel(self.xy, self.text, self.font, cell_shape, 
            self.fill_pen, self.width, self.height, self.fill_jitter)
         result.append(fill)
      return result

