#!/usr/bin/env python

'''Read in a data file and plot it using a virtual plotter.'''

from chiplotle import *
from chiplotle.tools.plottertools import instantiate_virtual_plotter

def main():

    plotter = instantiate_virtual_plotter(Coordinate(0, 0), Coordinate(30000, 20000))

    data_file = open("./media/indoor_temp.txt", 'r')
    
    data = data_file.readlines()
    
    print "read %d data points." % len(data)

    #make an empty list and fill it with data points as coordinates
    points = []
    x = 0
    
    for y in data:
        #we use rstrip() to remove the line break
        y_value = eval(y.rstrip()) * 100
        #print "y_value: %f" % y_value
        c = Coordinate(x, y_value)
        points.append(c)
        x += 10
        
    data_path = shapes.path(points)
    
    plotter.select_pen(4)
    plotter.write(data_path)
    
    #let's offset it and plot it again!
    
    offset(data_path, (1000, 1000))
    plotter.select_pen(5)
    plotter.write(data_path)
    
    #let's draw a box around our offset plot
    (min, max) = data_path.minmax_coordinates
    (width, height) = max - min

    r = shapes.rectangle(width, height)
    
    #a rectangle has its center at (0,0)
    #so we shift it over so that its lower, left corner is (0,0)
    #and we shift it some more to fit around our offset data
    transforms.offset(r, (width/2, height/2))
    transforms.offset(r, min)
    
    plotter.select_pen(6)
    plotter.write(r)
    
    #take a looksee!
    io.view(plotter)

### run main if called from command line like so: 
### $> python data_do_path.py
if __name__ == '__main__': main()

