#!/usr/bin/env python

from chiplotle import *
from chiplotle.tools import *
import random
import sys


def abstract_masterpiece_file(file):

   saved = False

   while not saved:
      plot = generate_plot()

      io.view(plot)

      saveit = raw_input("\nsave this one (y/n)? ")
      if 'y' in saveit:
         io.save_hpgl(plot, file)
         print "saved " + file
         saved = True

   print "bye!"

def generate_plot():

   width = 30000
   height = 20000
   left = 0
   right = 30000
   bottom = 0
   top = 20000

   print "width: %d height: %d" % (width, height)
   pens = raw_input("\nhow many pens do you want to use? ")
   numPens = int(pens)
   
   plot = []
   
   #start in a random spot
   
   plot.append(PA([random.randint(left, right), random.randint(bottom, top)]))

   penNum = 1
   
   while True:
       #plotter.select_pen(penNum)
       plot.append(SP(penNum))

       whichGesture = random.randint(0,5)
       
       if whichGesture == 0:
           print "circle!"
           #plotter.circle(random.randint(10,5000), random.randint(1,180))
           x = random.randint(left, right)
           y = random.randint(bottom, top)
           plot.append(CI(random.randint(10,5000), random.randint(1,180)))
       
       
       elif whichGesture == 1:
           print "rect!"
           x = random.randint(left, right)
           y = random.randint(bottom, top)
           #plotter.edgeRectRelative(random.randint(10,5000), random.randint(10,5000))        
           plot.append(ER([random.randint(10,5000), random.randint(10,5000)]))

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
           #plotter.fill_type(ft, space, angle)
           #plotter.shadeRectRelative(random.randint(10,2000), random.randint(10,2000))
           plot.append(FT(ft, space, angle))
           plot.append(RR([random.randint(10,2000), random.randint(10,2000)]))
           

       elif whichGesture == 3:
           print "draw a crazy line!"
           #plotter.pen_down()
           #plotter.goto(random.randint(left, right), random.randint(bottom, top))
           #plotter.pen_up()
           plot.append(PD())
           plot.append(PA([random.randint(left, right), random.randint(bottom, top)]))
           plot.append(PU())
           
           
       elif whichGesture == 4:
           print "draw an abstract shape!"
           numPoints = random.randint(2,4)
           print "numPoints: ", numPoints
           firstX = random.randint(left, right)
           firstY = random.randint(bottom, top)
           #plotter.goto(firstX, firstY)
           #plotter.pen_down()
           plot.append(PA([firstX, firstY]))
           plot.append(PD())
           
           xRange = width/5
           yRange = height/5
                   
           for i in range(numPoints):
              #plotter.nudge(random.randint(int(-xRange), int(xRange)), random.randint(int(-yRange), int(yRange)))
              plot.append(PR([random.randint(int(-xRange), int(xRange)), random.randint(int(-yRange), int(yRange))]))
              
           
           #plotter.goto(firstX, firstY)
           #plotter.pen_up()
           
           plot.append(PA([firstX, firstY]))
           plot.append(PU())
           
       elif whichGesture == 5:
           print "just jump around!"
           #plotter.goto(random.randint(left, right), random.randint(bottom, top))
           plot.append(PA([random.randint(left, right), random.randint(bottom, top)]))
           
       #pick a new pen?
       pickPen = random.randint(0,99)
       if pickPen < 25:
           penNum += 1

       if penNum == numPens + 1:
           break
   
   plot.append(SP(0))
   
   return plot
   


### run main if called from command line like so: 
### $> python abstract_masterpiece.py
if __name__ == '__main__':
   if len(sys.argv) < 2:
      print 'Must give output filename.\nExample: $ abstract_masterpiece_file.py myfile.hpgl'
      sys.exit(2)
   file = sys.argv[1]

   abstract_masterpiece_file(file) 
