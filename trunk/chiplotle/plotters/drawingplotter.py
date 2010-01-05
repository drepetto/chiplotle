
from chiplotle.plotters.baseplotter import _BasePlotter

class _DrawingPlotter(_BasePlotter):

   ## TEXT OUTPUT & SETTINGS ##

   def absoluteCharSize(self, w = None, h = None):
      self.write(self._hpgl.SI(w, h))

   def absoluteDirection(self, run = 1, rise = 0):
      print 'not implemented yet.'

   def altCharSet(self, n = 0):
      self.write(self._hpgl.CA(n))

   def charChordAngle(self, angle = 5):
      self.write(self._hpgl.CC(angle))

   def bufferLabel(self, text = None):
      self.write(self._hpgl.BL(text))

   def charPlot(self, spaces = None, lines = None):
      self.write(self._hpgl.CP(spaces, lines))

   def charSelectionMode(self, switch = 0, fallback = 0):
      self.write(self._hpgl.CM(switch, fallback))

   def charSet(self, set = 0):
      self.write(self._hpgl.CS(set))        

   def charSlant(self, tan = 0):
      self.write(self._hpgl.SL(tan))

   def defineLabelTerminator(self, t = chr(3)):
      self.write(self._hpgl.DT(t))

#   def directionVertical(self, dir = 0):
#   self.write(self._hpgl.directionVertical(dir))

#   def extraSpace(self, spaces = 0, lines = 0):
#   self.write(self._hpgl.extraSpace(spaces, lines))

#   def invokeCharSlant(self, slot = 0, left = None):
#   self.write(self._hpgl.invokeCharSlant(slote, left))

   def label(self, text):
      self.write(self._hpgl.LB(text))

#   def labelOrigin(self, positionNum = 1):
#   self.write(self._hpgl.labelOrigin(positionNum))

#   def newLine(self):
#   self.write(self._hpgl.newLine())


   def printBufferedLabel(self):
      self.write(self._hpgl.PB())

   def relCharSize(self, w = None, h = None):
      self.write(self._hpgl.SR(w, h))

#   def relativeDirection(self, run = 1, rise = 0):
#   self.write(self._hpgl.relativeDirection(run, rise))
          
   def selectAltCharSet(self):
      self.write(self._hpgl.SA())

   def symbolMode(self, char = None):
      self.write(self._hpgl.SM(char))

   def selectStandardCharSet(self):
      self.write(self._hpgl.SS())



   ## DRAWING PRIMITIVES & SETTINGS

   def arcAbsolute(self, x, y, aa, ca = 5):
      self.write(self._hpgl.AA((x, y), aa, ca))

   def arcRelative(self, x, y, aa, ca = 5):
      self.write(self._hpgl.AR((x, y), aa, ca))

   def chordTolerance(self, type = 0):
      self.write(self._hpgl.CT(type))

   def circle(self, rad, ca = 5):
      self.write(self._hpgl.CI(rad, ca))

#   def curvedLineGenerator(self, n = None, inputDelay = None):
#   self.write(self._hpgl.curvedLineGenerator(n, inputDelay))

   def edgePolygon(self):
      self.write(self._hpgl.EP())

   def edgeRectRelative(self, x, y):
      self.write(self._hpgl.ER((x,y)))

   def edgeRectAbsolute(self, x, y):
      self.write(self._hpgl.EA((x,y)))

#   def edgeWedge(self, r, sa, swa, ca=5):
#   self.write(self._hpgl.edgeWedge(r, sa, swa, ca))

   def fillPolygon(self):
      self.write(self._hpgl.FP())

   def fillType(self, type=1, space=None,  angle=0):
      self.write(self._hpgl.FT(type, space, angle))

   def lineType(self, pattern, length = 4):
      self.write(self._hpgl.LT(pattern, length))

   def plotPolygon(self, n = 0):
      self.write(self._hpgl.PM(n))

   def shadeRectAbsolute(self, x, y):        
      self.write(self._hpgl.RA((x, y)))

   def shadeRectRelative(self, x, y):
      self.write(self._hpgl.RR((x, y)))

#   def shadeWedge(self, r, sa, swa, ca = 5):
#   self.write(self._hpgl.shadeWedge(r, sa, swa, ca))


   ## DIRECT PEN CONTROL & INFO

   def accelSelect(self, accel = None, pen = None):
      self.write(self._hpgl.AS(accel, pen))

   def forceSelect(self, force = None, pen = None):
      self.write(self._hpgl.FS(force, pen))

   def goto(self, x, y):
      """Alias for PA() with only one point"""
      self.write(self._hpgl.PA((x, y)))

   def goto_center(self):
      self.write(self._hpgl.PA(self.margins.soft.center))

   def goto_bottom_left(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_left))

   def goto_bottom_right(self):
      self.write(self._hpgl.PA(self.margins.soft.bottom_right))

   def goto_top_left(self):
      self.write(self._hpgl.PA(self.margins.soft.top_left))

   def goto_top_right(self):
      self.write(self._hpgl.PA(self.margins.soft.top_right))

   def nudge(self, x, y):
      self.write(self._hpgl.PR((x,y)))

   def plotAbsolute(self, coords = None):
      """
         Plot Absolute.
         Takes a tuple of any number of sets of points:
         (0,0,100,100,2500,1000) will go to three different points:
             0,0 100,100 2500,1000
      """
      self.write(self._hpgl.PA(coords))

   def plotRelative(self, coords = None):
      """
         Plot Relative.
         Takes a tuple of any number of sets of points:
         (0,0,100,100,2500,1000) will go to three different points:
             0,0 100,100 2500,1000
      """
      self.write(self._hpgl.PR(coords))

   def penDown(self, coords = None):
      """Pen Down."""
      self.write(self._hpgl.PD(coords))

   def penThickness(self, thickness = 0.3):
      self.write(self._hpgl.PT(thickness))

   def penUp(self, coords = None):
      """Pen Up."""
      self.write(self._hpgl.PU(coords))

   def selectPen(self, penNum = 0):
      self.write(self._hpgl.SP(penNum))

   def tickLength(self, tp = 0.5, tn = 0.5):
      self.write(self._hpgl.TL(tp, tn))

   def xTick(self):
      self.write(self._hpgl.XT())

   def yTick(self):
      self.write(self._hpgl.YT())        
              
   def velocitySelect(self, v = None, pen = None):
      """ Set pen's velocity."""
      self.write(self._hpgl.VS(v, pen))

   def inputWindow(self, xLL = None, yLL = None, xUR = None, yUR = None):
      self.write(self._hpgl.IW((xLL, yLL, xUR, yUR)))

   def paperSize(self, size = None):
      self.write(self._hpgl.PS(size))

   def rotate(self, angle = 0):
      self.write(self._hpgl.RO(angle))

   def scale(self, xMin, xMax, yMin, yMax):
      self.write(self._hpgl.SC((xMin, xMax, yMin, yMax)))


   ## PAPER CONTROLS

   def advanceFrame(self):
      self.write(self._hpgl.FR())

   def advanceFullPage(self):
      self.write(self._hpgl.AF())

   def advanceHalfPage(self):
      self.write(self._hpgl.AH())   

   def enableCutLine(self, n):
      self.write(self._hpgl.EC(n))

   def pageFeed(self, n = None):
      self.write(self._hpgl.PG(n))


   ## DIGITIZER CONTROLS

   def clearDigitizer(self):
      self.write(self._hpgl.DC())

   def digitizePoint(self):
      self.write(self._hpgl.DP())


   ## MISC I/O, PLOTTER QUERIES, ERRORS, SETUP

   def abortCommand(self):
      """Tells the plotter to discard commands in its buffer."""
      self.write(self._hpgl.K())

   def automaticPen(self, p = None):
      self.write(self._hpgl.AP(p))

   def bufferPlot(self):
      self.write(self._hpgl.BF())

   def defaultInstruction(self):
      self.write(self._hpgl.DF())

#   def defineKey(self, key = None, function = None):
#      self.write(self._hpgl.defineKey())


#   def inputMask(self, e = 233, s = 0, p = 0):
#   self.write(self._hpgl.inputMask(e, s, p))

   def notReady(self):
      '''what's this for?'''
      self.write(self._hpgl.NR())

   def replot(self, n = 1):
      self.write(self._hpgl.RP(n))

   def writeToDisplay(self, text):
      self.write(self._hpgl.WD(text))


#   def escapeHS2(self, minbytes=81, xon='17'):
#   self.writeControl(self._hpgl.escapeHS2(minbytes, xon))
#   self.xon = str(xon) 
#
#   def escapeXoff(self, xoff='19', interchar_speed=0):
#   self.writeControl(self._hpgl.escapeXoff(xoff, interchar_speed))
#   self.xoff = str(xoff)
