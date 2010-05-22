from chiplotle import *

hpglcommands = [PA((10, 10)), PD( ), PA((10, 0)), PA((0, 0))]
print '\nA list of primitive HPGL commands.'
print hpglcommands

hpglcontainer = HPGLContainer((100, 100), hpglcommands)

print '\nPuting "primitive" HPGL commands in an HPGLContainer allows one to'
print 'carry them around as one object *and* to transpose them easily by'
print 'changing the xy position of the HPGLContainer.'

print '\nThis is the string format of the HPGLContainer with position (100, 100):'
print hpglcontainer.format

