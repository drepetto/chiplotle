from chiplotle import *

plotter = instantiate_plotters( )[0]
plotter.set_origin_center( )

## draw slowly so we see what's going on:
plotter.write(VS(4))
## draw a reference (0,0) point:
plotter.write(Circle((0,0), 100))

## A Group always has a position:
g1 = Group((1000, 2000))
print 'g1 position: ', g1.xy

## A Group can take both HPGL primitives and compound HPGL commands:
g1 = Group((1000, 2000), [Rectangle((0, 0), 500, 300), CI(200, 120)]) 

plotter.write(g1)


## Groups can be nested:
g2 = Group((-4000, -2000), [g1, LB('g1 in g2')])

plotter.write(g2)


## The same group (g1) or any other Chiplotle HPGL instance can be 
## inserted in other groups:
g3 = Group((0, -2000), [g1, LB('g1 in g3')])

plotter.write(g3)

