from chiplotle import *

p = instantiate_plotters()[0]
p.select_pen(1)

## base of the equilateral triangle
t_base = 4000

points = [(-t_base/2,0),(0,t_base*0.8660),(t_base/2,0)]

## a list containing different sets of weights for the middle point
weights = [[1,1,1],[1,2,1],[1,0.5,1],[1,0,1],[1,-0.5,1]]

c = Container((0,0))

## draws a cross at each control point
for i in points:
   r = Cross(i,100,100)
   c.append(r)

## draws the rational bezier curve for each weight set
for w in weights:
   b = Bezier(points, weight=w)
   c.append(b)

#io.view(c, format='png')

p.write(c.format)
p.select_pen(0)
