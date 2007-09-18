"""
 *  Copyright 2007 Douglas Repetto and Victor Adan
 *
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
 *
 *  chiplotlib is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License version 2 as
 *  published by the Free Software Foundation.
 *
 *  chiplotlib is distributed in the hope that it will be useful, but
 *  WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 *  General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with chiplotle; if not, write to the Free Software
 *  Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA
 *  02110-1301 USA
 *
 *  See the file "COPYING" for the text of the license.
"""


import os
import re
import serial
import chiplotle
import commands_generic_hpgl

print "chiplotle in the house.\n"


availablePorts = os.listdir("/dev")
ttyTest = re.compile("tty\.")
ttys = filter(ttyTest.search, availablePorts)   

print "available ports:\n"
i = 0
for port in ttys:
    print "[%d] %s" % (i, port)
    i += 1

print "[%d] write to file" % i
i += 1

# raw_input() reads every input as a string
# then it's up to you to process the string
sp = raw_input("\nuse serial port [0 - %d]: " % (i - 1))

if int(sp) < (i - 2):
    print "okay, opening %s..." % ttys[int(sp)]
    ser = serial.Serial("/dev/" + ttys[int(sp)], 9600, timeout=1)
    p = chiplotle.Plotter(ser)
else:
    print "writing to file."
    fn = raw_input("filename: ")
    p = chiplotle.Plotter(ser = "null", writeToSerial = False, writeToFile = True,
        defaultFileName = fn)
    p.startFileOutput()

p.lang.setPlotterType(commands_generic_hpgl.plotterType)
p.lang.setAllowedCommands(commands_generic_hpgl.allowedHPGLCommands)

print "\n"
print "plotter ID: " + p.plotterID
print "margins: left: %d right: %d bottom: %d top: %d" % (p.left(), p.right(), p.bottom(), p.top())
print "centerX: %d centerY: %d" % (p.centerX(), p.centerY())


availableCommands = os.listdir("./")
def commandTest(name):
    if name.startswith("command"):
        if name.endswith("py"):
            return name
            
commands = filter(commandTest, availableCommands)   

print "\navailable command sets:\n"
i = 0
for set in commands:
    if set.endswith("pyc"):
        pass
    else:
        print "[%d] %s" % (i, set)
        i += 1

c = raw_input("\nimport command set [0 - %d]: " % (i - 1))

if c:
    cName = commands[int(c)]

    import_name = cName.strip(".py")
    print "\nimporting: " + import_name
    importedCommands = __import__(import_name)
    p.lang.setPlotterType(importedCommands.plotterType)
    p.lang.setAllowedCommands(importedCommands.allowedHPGLCommands)



