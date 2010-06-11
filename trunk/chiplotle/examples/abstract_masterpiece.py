#!/usr/bin/env python

from chiplotle import *
import random

def main():

   plotter = instantiate_plotters( )[0]

   width = plotter.margins.soft.width
   height = plotter.margins.soft.height
   left = plotter.margins.soft.left
   right = plotter.margins.soft.right
   bottom = plotter.margins.soft.bottom
   top = plotter.margins.soft.top

   print "width: %d height: %d" % (plotter.margins.soft.width, plotter.margins.soft.height)
   pens = raw_input("\nhow many pens do you want to use? ")
   numPens = int(pens)

   #start in a random spot
   plotter.goto(random.randint(left, right), random.randint(bottom, top))
   penNum = 1

   while True:
       plotter.select_pen(penNum)

       whichGesture = random.randint(0,5)
       
       if whichGesture == 0:
           print "circle!"
           plotter.circle(random.randint(10,5000), random.randint(1,180))
       
       elif whichGesture == 1:
           print "rect!"
           plotter.write(ER((random.randint(10,5000), random.randint(10,5000))))        

       elif whichGesture == 2:
           print "filled rect!"
           ft = random.randint(1,8)
           if ft == 1 or ft == 2:
               ft = 1
           if ft == 3 or ft == 4 or ft == 5:
               ft = 3
           if ft == 6 or ft == 7 or ft == 8:
               ft = 4
               
           space = random.randint(10,100)
           angle = random.randint(0,3) * 45
           
           print "fill type: %d space: %d angle: %d" % (ft, space, angle)
           plotter.fill_type(ft, space, angle)
           #plotter.shade_rectangle_relative(random.randint(10,2000), random.randint(10,2000))
           plotter.filled_rectangle_relative(random.randint(10,2000), random.randint(10,2000))

       elif whichGesture == 3:
           print "draw a crazy line!"
           plotter.pen_down()
           plotter.goto(random.randint(left, right), random.randint(bottom, top))
           plotter.pen_up()
           
       elif whichGesture == 4:
           print "draw an abstract shape!"
           numPoints = random.randint(2,4)
           print "numPoints: ", numPoints
           firstX = random.randint(left, right)
           firstY = random.randint(bottom, top)
           plotter.goto(firstX, firstY)
           plotter.pen_down()
           xRange = width/5
           yRange = height/5
                   
           for i in range(numPoints):
               plotter.nudge(random.randint(int(-xRange), int(xRange)), random.randint(int(-yRange), int(yRange)))
           plotter.goto(firstX, firstY)
           plotter.pen_up()
           
       elif whichGesture == 5:
           print "just jump around!"
           plotter.goto(random.randint(left, right), random.randint(bottom, top))
           
       #pick a new pen?
       pickPen = random.randint(0,99)
       if pickPen < 25:
           penNum += 1

       if penNum == numPens + 1:
           break
           
   plotter.select_pen(0)

### run main if called from command line like so: 
### $> python abstract_masterpiece.py
if __name__ == '__main__': main()
