#!/usr/bin/env python

'''A simple example that shows how to load existing hpgl code into chiplotle.'''

from chiplotle import *
from chiplotle.tools.io.import_hpgl_file import import_hpgl_file
from chiplotle.tools.plottertools import instantiate_virtual_plotter

import time

def main():

    print 'Importing media/square.hpgl'
    f = import_hpgl_file("./media/square.hpgl")

    print "Here are the contents of the file, expanded into a list of chiplotle objects:"
    print f
    
    print "\nAnd here are the raw hpgl commands:"
    
    for c in f:
        print c.format

    # We can use io.view() to take a look...
    io.view(f)
    
    # small delay to give our external postscript reader time to 
    # load the output file
    time.sleep(1)
    
    # We can also send the commands to a plotter. 
    # We'll use a virtual plotter in this example:
    plotter = instantiate_virtual_plotter()

    # Now we'll send the contents of the file to the plotter 
    # so we can take a look.
    plotter.write(f)
    
    # And now we'll use io.view() to view what the virtual plotter has drawn.
    io.view(plotter)
    time.sleep(1)

    # We know from looking at the contents of the file above that the first thing
    # the hpgl code does is select pen 1. Let's change that to pen 2:
    
    print "\nbefore:"
    print f[0]

    f[0] = hpgl.SP(2)
    
    print "\nafter:"    
    print f[0]
    
    # We'll clear the virtual plotter so that we can start a new drawing:
    plotter.clear()
    
    plotter.write(f)
    
    # now we should see the same plot with a different color
    io.view(plotter)
    time.sleep(1)


    # Now maybe I want to add a little somethingsomething:
    c = shapes.circle(1000)
    
    # insert the plotter into the list of commands at the position just before
    # the last pen up (PU;) command:
    f.insert(len(f) - 1, c)
    
    print "\nWe've inserted a circle (Path) into the list of commands:"
    print f
    
    plotter.clear()
    plotter.select_pen(3)
    plotter.write(f)

    io.view(plotter)
   

if __name__ == '__main__': main()
