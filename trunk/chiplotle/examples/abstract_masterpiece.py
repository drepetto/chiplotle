from chiplotle import *
import random


def main():

   plotter = instantiate_plotter( )

   width = plotter.marginSoft.width
   height = plotter.marginSoft.height
   left = plotter.marginSoft.left
   right = plotter.marginSoft.right
   bottom = plotter.marginSoft.bottom
   top = plotter.marginSoft.top

   print "width: %d height: %d" % (plotter.marginSoft.width, plotter.marginSoft.height)
   pens = raw_input("\nhow many pens do you want to use? ")
   numPens = int(pens)

   #start in a random spot
   plotter.goto(random.randint(left, right), random.randint(bottom, top))
   penNum = 1

   while True:
       plotter.selectPen(penNum)

       whichGesture = random.randint(0,5)
       
       if whichGesture == 0:
           print "circle!"
           plotter.circle(random.randint(10,5000), random.randint(1,180))
       
       elif whichGesture == 1:
           print "rect!"
           plotter.edgeRectRelative(random.randint(10,5000), random.randint(10,5000))        

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
           
           print "fillType: %d space: %d angle: %d" % (ft, space, angle)
           plotter.fillType(ft, space, angle)
           plotter.shadeRectRelative(random.randint(10,2000), random.randint(10,2000))

       elif whichGesture == 3:
           print "draw a crazy line!"
           plotter.penDown()
           plotter.goto(random.randint(left, right), random.randint(bottom, top))
           plotter.penUp()
           
       elif whichGesture == 4:
           print "draw an abstract shape!"
           numPoints = random.randint(2,4)
           print "numPoints: ", numPoints
           firstX = random.randint(left, right)
           firstY = random.randint(bottom, top)
           plotter.goto(firstX, firstY)
           plotter.penDown()
           xRange = width/5
           yRange = height/5
                   
           for i in range(numPoints):
               plotter.nudge(random.randint(-xRange, xRange), random.randint(-yRange, yRange))
           plotter.goto(firstX, firstY)
           plotter.penUp()
           
       elif whichGesture == 5:
           print "just jump around!"
           plotter.goto(random.randint(left, right), random.randint(bottom, top))
           
       #pick a new pen?
       pickPen = random.randint(0,99)
       if pickPen < 25:
           penNum += 1

       if penNum == numPens + 1:
           break
           
   plotter.selectPen(0)

### run main if called from command line like so: 
### $> python abstract_masterpiece.py
if __name__ == '__main__': main()
