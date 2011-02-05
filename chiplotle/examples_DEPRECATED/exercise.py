'''
Draws various grids, excercising plotter. A good way to verify that plotter 
is working as intended and to find any trouble spots in x/y travel.
'''


from chiplotle import *

plotter = instantiate_plotters( )[0]
plotter.set_origin_bottom_left()

width = plotter.margins.hard.width
width_incr = int(width/10)
height = plotter.margins.hard.height
height_incr = int(height/10)

print "Plotter, you need some excercise! Let's go!"
print "width: %d height: %d width_incr: %d height_incr: %d" % \
    (width, height, width_incr, height_incr)

x = 0
y = 0

exercise = []

plotter.select_pen(1)

print "doing vertical..."

for i in range(6):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([x, y]))
    exercise.append(PD())
    exercise.append(PA([x, height]))
    exercise.append(PU())

    x += width_incr

    if i < 5:
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([x, height]))
        exercise.append(PD())
        exercise.append(PA([x, 0]))
        exercise.append(PU())
        
        x += width_incr

plotter.write(exercise)

print "doing horizontal..."

exercise = []
y = height
    
for i in range(6):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([width, y]))
    exercise.append(PD())
    exercise.append(PA([0, y]))
    exercise.append(PU())

    y -= height_incr

    if i < 5:
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([0, y]))
        exercise.append(PD())
        exercise.append(PA([width, y]))
        exercise.append(PU())
        
        y -= height_incr    
    
plotter.write(exercise)


print "doing left to right diag..."

exercise = []
x = 0
y = 0

for i in range(10):
    y += height_incr
    x += width_incr
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([0, y]))
    exercise.append(PD())
    exercise.append(PA([x, 0]))
    exercise.append(PU())

    if i < 9:
        y += height_incr
        x += width_incr
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([x, 0]))
        exercise.append(PD())
        exercise.append(PA([0, y]))
        exercise.append(PU())
    

plotter.write(exercise)


print "doing down up diag..."

exercise = []
x = width
y = 0

for i in range(10):
    y += height_incr
    x -= width_incr
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([width, y]))
    exercise.append(PD())
    exercise.append(PA([x, 0]))
    exercise.append(PU())

    if i < 9:
        y += height_incr
        x -= width_incr
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([x, 0]))
        exercise.append(PD())
        exercise.append(PA([width, y]))
        exercise.append(PU())
    

plotter.write(exercise)

print "doing 0,0 fan..."

exercise = []
x = 0
y = 0

for i in range(6):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([0, 0]))
    exercise.append(PD())
    exercise.append(PA([x, height]))
    exercise.append(PU())

    x += width_incr
    
    if i < 5:
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([x, height]))
        exercise.append(PD())
        exercise.append(PA([0, 0]))
        exercise.append(PU())
        
    x += width_incr
    
y = height - height_incr

for i in range(5):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([width, y]))
    exercise.append(PD())
    exercise.append(PA([0, 0]))
    exercise.append(PU())

    y -= height_incr

    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([0, 0]))
    exercise.append(PD())
    exercise.append(PA([width, y]))
    exercise.append(PU())
        
    y -= height_incr

plotter.write(exercise)


print "doing width,0 fan..."

exercise = []
x = width
y = 0

for i in range(6):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([width, 0]))
    exercise.append(PD())
    exercise.append(PA([x, height]))
    exercise.append(PU())

    x -= width_incr
    
    if i < 5:
        print "x: %d y:%d i: %d" % (x, y, i)
        exercise.append(PA([x, height]))
        exercise.append(PD())
        exercise.append(PA([width, 0]))
        exercise.append(PU())
        
    x -= width_incr
    
y = height - height_incr

for i in range(5):
    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([0, y]))
    exercise.append(PD())
    exercise.append(PA([width, 0]))
    exercise.append(PU())

    y -= height_incr

    print "x: %d y:%d i: %d" % (x, y, i)
    exercise.append(PA([width, 0]))
    exercise.append(PD())
    exercise.append(PA([0, y]))
    exercise.append(PU())
        
    y -= height_incr

plotter.write(exercise)

raw_input("press enter when finished...")
