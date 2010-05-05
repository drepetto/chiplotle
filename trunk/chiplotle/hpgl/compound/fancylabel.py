from __future__ import division
from chiplotle.utils.ispair import ispair
from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PA, PR, PU, SP
import copy
import random


class FancyLabel(_CompoundHPGL):
   '''FancyLabel.
   
   Write text with arbitrary Chiplotle-font and arbitrary cell shape.
   
   * `xy`: (x, y) position of the label.
   * `text`: a string of the text to be printer.
   * `font`: the Chiplotle-font to use. This should be a valid Chiplotle-font.
      Chiplotle-fonts live in chiplotle/fonts.
   * `cell_shape` : the Chiplotle-HPGL shape to use to draw each cell.
      These can be simple Chiplotle-HPGL commands or Compound commands.
   * `pen`: the pen to use [1 to 8].
   * `width`: the width of each character. May be a number or None.
   * `height`: the height of each character. May be a number or None.
   * `jitter` : an (x, y) tuple indicating the ammount of randomness added
      to each of the cells making up each character. 
   '''
   def __init__(self, xy, text, font, cell_shape, pen=None, 
      width=None, height=None, jitter = None):
      _CompoundHPGL.__init__(self, xy, pen)
      self.cell_shape = cell_shape
      self.text = text
      ## handle font
      if not hasattr(font, 'char_dict'):
         raise ValueError('`font` is not a valid Matrix-Font file.')
      self.font = font
      ## handle jitter
      if not ispair(jitter) and jitter is not None:
         raise ValueError('`jitter` must be of the form (x, y) or None.')
      self.jitter = jitter or (0, 0)
      ## handle width and height input parameters
      if not (width or height):
         raise ValueError('At least width or height must be given.')
      self.width = width
      self.height = height
      h = len(self.font.char_dict['a'])
      w = len(self.font.char_dict['a'][0])
      if width and not height:
         self.height = h / w * width
      elif height and not width:
         self.width =  w / h * height

   
   def _get_cell(self, x, y):
      command = copy.deepcopy(self.cell_shape)
      if isinstance(command, _CompoundHPGL):
         command.xy = (x, y)
         return [command]
      else:
         return [PA((x, y)), command]


   def _get_text(self):
      random.seed()
      result = [ ]      
      width_margin = self.width / 4.
      x = self.xabsolute
      y = self.yabsolute
      for i, char in enumerate(self.text):
         abs_position = (x, y)
         result.extend(self._get_character(char, abs_position))     
         x = x + self.width + width_margin

      return result


   def _get_character(self, char, abs_pos):
      result = [ ]
      character = self.font.char_dict[char]
      shape = [0,0]
      rows = len(self.font.char_dict['a'])
      cols = len(self.font.char_dict['a'][0])
   
      for r in range(rows):
         for c in range(cols):
            x = abs_pos[0]
            x = x + c * self.width / cols
            x = x + random.gauss(0, self.jitter[0])
            y = abs_pos[1]
            y = y + r * self.height / rows
            y = y + random.gauss(0, self.jitter[1])

            value = character[rows - 1 - r][c]
            if value == 1:
               result.extend(self._get_cell(x, y))

      return result         
      
   

   @property
   def _subcommands(self):
      result = _CompoundHPGL._subcommands.fget(self)
      result += [PU( ), PA(self.xyabsolute)]
      result += self._get_text( )
      return result
