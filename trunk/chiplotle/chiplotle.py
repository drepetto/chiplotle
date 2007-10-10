
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from languages import chiplotle_hpgl
from languages import  utils
import math

class Grob(object):
    def __init__(self, x, y, **kwargs):
        self.x = x
        self.y = y

        self.lang = chiplotle_hpgl
        if kwargs.has_key('lang'):
            self.lang = kwargs['lang']
            kwargs.pop('lang')

        self.rot = 0
        if kwargs.has_key('rot'):
            self.rot = kwargs['rot']
            kwargs.pop('rot')

        self.color = 1
        if kwargs.has_key('color'):
            self.color = kwargs['color']
            kwargs.pop('color')

        self.line_type = None
        if kwargs.has_key('line_type'):
            self.line_type = kwargs['line_type']
            kwargs.pop('line_type')

        
    def draw(self):
        pass



# ---------------------------------
class Rectangle(Grob):
    def __init__(self, x, y, **kwargs):
        self.sx = 1
        if kwargs.has_key('sx'):
            self.sx = kwargs['sx']
            kwargs.pop('sx')

        self.sy = 1
        if kwargs.has_key('sy'):
            self.sy = kwargs['sy']
            kwargs.pop('sy')

        self.fill = False
        if kwargs.has_key('fill'):
            self.fill = kwargs['fill']
            kwargs.pop('fill')

        Grob.__init__(self, x, y, **kwargs)

    
    def draw(self):
        if self.fill:
            pass
        else:
            return self.lang.edgeRect(self.x, self.y, self.sx, self.sy, self.rot)

    @property
    def left(self):
        return self.x - self.sx / 2. 
    @property
    def right(self):
        return self.x + self.sx / 2. 
    @property
    def top(self):
        return self.y + self.sy / 2. 
    @property
    def bottom(self):
        return self.y - self.sy / 2. 


class Circle(Grob):
    def __init__(self, x, y, **kwargs):
        self.rad = 1
        if kwargs.has_key('rad'):
            self.rad = kwargs['rad']
            kwargs.pop('rad')

        self.fill = False
        if kwargs.has_key('fill'):
            self.fill = kwargs['fill']
            kwargs.pop('fill')

        Grob.__init__(self, x, y, **kwargs)


    def draw(self):
        if self.fill:
            pass
        else:
            return self.lang.edgeCircle(self.x, self.y, self.rad)


class Spiral(Grob):
    def __init__(self, x, y, delta_y=10, rot=3.1415/16, **kwargs ):
        self.delta_y = delta_y
        self.rot = rot
        Grob.__init__(self, x, y, **kwargs)

    def draw(self):
        out = self.lang.penUp()
        out += self.lang.plotAbsolute((self.x, self.y))
        out += self.lang.lineRelative(self.sx)
    
        while self.sx > 2:
            self.y += self.delta_y
            #self.x += self.delta_x
            self.rot += self.rot
            self.sx *= self.factor_size

            out += self.draw()

        return out

def spiral(x, dy, rot):
    if math.sqrt(dy**2 + x**2) <= 1:
        return ''
    out = ''
    out += chiplotle_hpgl.penDown()
    out += chiplotle_hpgl.plotRelative((x, dy))
    (x, dy) = utils.rotate2d((x,dy), rot)
    return out + spiral(x, dy/1.1, rot)

    
