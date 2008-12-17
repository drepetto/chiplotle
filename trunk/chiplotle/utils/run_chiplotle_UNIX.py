
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from chiplotle import *
from chiplotle.utils.open_serial import open_serial


print "\n* * * CHIPLOTLE in the house! * * *\n"

ser = open_serial( )
print ser

p = plotters.Plotter(ser)
print "\nPlotter with ID %s found in selected port." % p.id

print "\nChoose a plotter type:"
for i, p in enumerate(dir(plotters)):
   print '[%d] %s' % (i,  p)

p = plotters.__dict__[ dir(plotters)[int(raw_input())] ](ser)

print "\nPlotter [p] with ID %s opened. " % p.id
print "Drawing area: %s" % p.marginSoft
print "Status: %s" % p.status


