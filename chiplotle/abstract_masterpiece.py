import random
import run_chiplotle_UNIX

from languages import chiplotle_hpgl as chpgl

p = run_chiplotle_UNIX.p

width = p.right() - p.left()
height = p.top() - p.bottom()

print "width: %d height: %d" % (width, height)

pens = raw_input("\nhow many pens do you want to use? ")
numPens = int(pens)

#start in a random spot
p.goto(random.randint(p.left(), p.right()), random.randint(p.bottom(), p.top()))

penNum = 1

while True:
    p.sp(penNum)

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
        p.pd()
        p.goto(random.randint(p.left(), p.right()), random.randint(p.bottom(), p.top()))
        p.pu()
        
    elif whichGesture == 4:
        print "draw an abstract shape!"
        numPoints = random.randint(2,4)
        print "numPoints: ", numPoints
        firstX = random.randint(p.left(), p.right())
        firstY = random.randint(p.bottom(), p.top())
        p.goto(firstX, firstY)
        p.pd()
        xRange = width/5
        yRange = height/5
                
        for i in range(numPoints):
            p.nudge(random.randint(-xRange, xRange), random.randint(-yRange, yRange))
        p.goto(firstX, firstY)
        p.pu()
        
    elif whichGesture == 5:
        print "just jump around!"
        p.goto(random.randint(p.left(), p.right()), random.randint(p.bottom(), p.top()))
        
    #pick a new pen?
    pickPen = random.randint(0,99)
    if pickPen < 25:
        penNum += 1

    if penNum == numPens + 1:
        break
        
p.sp(0)

