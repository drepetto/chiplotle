import random
import run_chiplotle_UNIX

from languages import chiplotle_hpgl as chpgl

c = run_chiplotle_UNIX.c

#start in a random spot
c.eat = chpgl.goto(random.randint(c.output.left(), c.output.right()), random.randint(c.output.bottom(), c.output.top()))

# how many gestures do we wnat to do?

#numGestures = random.randint(2,20)

#for gesture in range(numGestures):

penNum = 1

while True:
    #print "gesture %d:" % gesture

    c.eat = chpgl.sp(penNum)

    whichGesture = random.randint(0,4)
    
    if whichGesture == 0:
        print "circle!"
        c.eat = chpgl.circle(random.randint(10,5000), random.randint(1,180))
    
    elif whichGesture == 1:
        print "rect!"
        c.eat = chpgl.edgeRectRelative(random.randint(10,5000), random.randint(10,5000))        

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
        c.eat = chpgl.fillType(ft, space, angle)
        c.eat = chpgl.shadeRectRelative(random.randint(10,2000), random.randint(10,2000))

    elif whichGesture == 3:
        print "draw a crazy line!"
        c.eat = chpgl.pd()
        c.eat = chpgl.goto(random.randint(c.output.left(), c.output.right()), random.randint(c.output.bottom(), c.output.top()))
        c.eat = chpgl.pu()
        
    elif whichGesture == 4:
        print "just jump around!"
        c.eat = chpgl.goto(random.randint(c.output.left(), c.output.right()), random.randint(c.output.bottom(), c.output.top()))
        
    #pick a new pen?
    pickPen = random.randint(0,99)
    if pickPen < 25:
        penNum += 1

    if penNum == 9:
        break
        
c.eat = chpgl.sp(0)

