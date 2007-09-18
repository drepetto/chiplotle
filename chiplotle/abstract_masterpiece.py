import random
import run_chiplotle_OSX

p = run_chiplotle_OSX.p

#start in a random spot
p.goto(random.randint(p.left(), p.right()), random.randint(p.bottom(), p.top()))

# how many gestures do we wnat to do?

#numGestures = random.randint(2,20)

#for gesture in range(numGestures):

keepGoing = True

penNum = 1

while keepGoing:
    #print "gesture %d:" % gesture

    p.sp(penNum)

    whichGesture = random.randint(0,4)
    
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
        print "just jump around!"
        p.goto(random.randint(p.left(), p.right()), random.randint(p.bottom(), p.top()))
        
    #pick a new pen?
    pickPen = random.randint(0,99)
    if pickPen < 25:
        penNum += 1

    if penNum == 9:
        keepGoing = False
        
p.sp(0)

