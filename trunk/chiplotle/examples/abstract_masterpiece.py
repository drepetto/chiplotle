from chiplotle.utils.run_chiplotle_UNIX import p
import random


def main():
   #p = run_chiplotle_UNIX.p

   width = p.marginSoft.width
   height = p.marginSoft.height
   left = p.marginSoft.left
   right = p.marginSoft.right
   bottom = p.marginSoft.bottom
   top = p.marginSoft.top

   print "width: %d height: %d" % (p.marginSoft.width, p.marginSoft.height)
   pens = raw_input("\nhow many pens do you want to use? ")
   numPens = int(pens)

   #start in a random spot
   p.goto(random.randint(left, right), random.randint(bottom, top))
   penNum = 1

   while True:
       p.selectPen(penNum)

       whichGesture = random.randint(0,5)
       
       if whichGesture == 0:
           print "circle!"
           p.circle(random.randint(10,5000), random.randint(1,180))
       
       elif whichGesture == 1:
           print "rect!"
           p.edgeRectRelative(random.randint(10,5000), random.randint(10,5000))        

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
           p.fillType(ft, space, angle)
           p.shadeRectRelative(random.randint(10,2000), random.randint(10,2000))

       elif whichGesture == 3:
           print "draw a crazy line!"
           p.penDown()
           p.goto(random.randint(left, right), random.randint(bottom, top))
           p.penUp()
           
       elif whichGesture == 4:
           print "draw an abstract shape!"
           numPoints = random.randint(2,4)
           print "numPoints: ", numPoints
           firstX = random.randint(left, right)
           firstY = random.randint(bottom, top)
           p.goto(firstX, firstY)
           p.penDown()
           xRange = width/5
           yRange = height/5
                   
           for i in range(numPoints):
               p.nudge(random.randint(-xRange, xRange), random.randint(-yRange, yRange))
           p.goto(firstX, firstY)
           p.penUp()
           
       elif whichGesture == 5:
           print "just jump around!"
           p.goto(random.randint(left, right), random.randint(bottom, top))
           
       #pick a new pen?
       pickPen = random.randint(0,99)
       if pickPen < 25:
           penNum += 1

       if penNum == numPens + 1:
           break
           
   p.selectPen(0)

### run main if called from command line like so: 
### $> python abstract_masterpiece.py
if __name__ == '__main__': main()
