
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

import os
import re
import serial
from chiplotle import *
from languages import chiplotle_hpgl as chpgl
from plotters import *


print "* * * CHIPLOTLE in the house! * * *\n"


# get available ports
availablePorts = os.listdir("/dev")
ttyTest = re.compile("tty")
ttys = filter(ttyTest.search, availablePorts)   

print "available ports:\n"
for i,port in enumerate(ttys):
    print "[%d] %s" % (i, port)

sp = raw_input("\nuse serial port [0 - %d]: " % (i - 1))

print "okay, opening %s..." % ttys[int(sp)]
ser = serial.Serial("/dev/" + ttys[int(sp)], 9600, timeout= 1)


# ------------------------
print "\nChoose a plotter:\a"
plt = raw_input("""1. generic plotter
2. DX1300
3. HP7475A
4. HP7550A
5. HP7595A
""")
if plt == '1':
    p = plotter.Plotter(ser)
elif plt == '2':
    p = dxy1300.DXY1300(ser)
elif plt == '3':
    p = hp7475a.HP7475A(ser)
elif plt == '4':
    p = hp7550A.HP7550A(ser)
elif plt == '5':
    p = hp7595a.HP7595A(ser)
else:
    print "Wrong choice moron!\a\a"
# ------------------------

# show plotter id, and margins
print "\n"
print "plotter ID: " + p.id
print "margins: left: %d right: %d bottom: %d top: %d" % (p.left(), p.right(), p.bottom(), p.top())
print "centerX: %d centerY: %d" % (p.centerX(), p.centerY())

c = Canvas(p)


