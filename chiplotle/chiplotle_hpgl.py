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



import math 

import commands_generic_hpgl


"""
    chiplotle implementation of many HPGL commands.

"""

class Hpgl:
    def __init__(self, terminator=';'):
        self.terminator = terminator
        self.plotterType = "generic_hpgl"
        self.allowedCommands = commands_generic_hpgl.allowedHPGLCommands
        #self.allowedHPGL2Commands = generic_hpgl.allowedHPGL2Commands
        
    def setPlotterType(self, pT):
        self.plotterType = pT
        
    def setAllowedCommands(self, aC):
        self.allowedCommands = aC

    #def setAllowedHPGL2Commands(self, aC):
    #    self.allowedHPGL2Commands = aC

    """
        HPGL translations
    """

    def arcAbsolute(self, x, y, aa, ca = 5):
		if 'AA' in self.allowedCommands:
			return 'AA%d,%d,%d,%d%s' % (x, y, aa, ca, self.terminator)
		else:
			return self.terminator
   
    def advanceFullPage(self):
        if 'AF' in self.allowedCommands:
            return 'AF%s' % (self.terminator)
        else:
            return self.terminator

    def advanceHalfPage(self):
        if 'AH' in self.allowedCommands:
            return 'AH%s' % (self.terminator)
        else:
            return self.terminator			
	
	def automaticPen(self, p = None):
		"""
			Automatic Pen operations
			
			for 7550:
			bit no	dec value	logic state	meaning
			0		1			1			lift pen if down too long without motion
			0		0			0			do not lift pen until PU received
			1		2			1			put pen away if too long without  motion
			1		0			0			do not put pen away until SP0 received
			2		4			1			do not get new pen until drawing starts
			2		0			0			get pen immediately after SP command
			3		8			1			merge all pen up moves
			3		0			0			do not merge all pen up moves

			default is 7 on 7550
			
			codes are 0 to 255 with default of 95 on the DraftMaster
		"""
        if 'AP' in self.allowedCommands:
			if p:
				return 'AP%d%s' % (p, self.terminator)
			else:
				return 'AP' + self.terminator
        else:
            return self.terminator			
	
    def arcRelative(self, x, y, aa, ca = 5):
		if 'AR' in self.allowedCommands:
			return 'AR%d,%d,%d,%d%s' % (x, y, aa, ca, self.terminator)
		else:
			return self.terminator

    def accelSelect(self, accel = None, pen = None):
		"""
			Acceleration Select
			Can be set per-pen or for all pens at once.

			default on 7550: 6
			default on DM: 4
		"""
		if 'AS' in self.allowedCommands:
			if accel:
				if pen:
					return 'AS%d,%d%s' % (accel, pen, self.terminator)
				else:
					return 'AS%d%s' % (accel, self.terminator)					
			else:
				return 'AS' + self.terminator
		else:
			return self.terminator	

    def bufferPlot(self):
		if 'BF' in self.allowedCommands:
			return 'BF%s' % (self.terminator)
		else:
			return self.terminator

    def bufferLabel(self, text = None):
		"""
			Stores first 150 chars of text in buffer for later printing
			and label length measurements.
		"""
		if 'BL' in self.allowedCommands:
			if text == None:
				return 'BL%s' % (self.terminator)
			else:
				return 'BL' + text + chr(3) + self.terminator
		else:
			return self.terminator

    def altCharSet(self, n = 0):
		if 'CA' in self.allowedCommands:
			return 'CA%d%s' % (n, self.terminator)
		else:
			return self.terminator

    def charChordAngle(self, angle = 5):
		if 'CC' in self.allowedCommands:
			return 'CC%d%s' % (angle, self.terminator)
		else:
			return self.terminator

    def circle(self, r, ca = 5):
        if 'CI' in self.allowedCommands:
            return 'CI%d,%d%s' % (r, ca, self.terminator)
        else:
            return self.terminator

    def charSelectionMode(self, switch = 0, fallback = 0):
        if 'CM' in self.allowedCommands:
            return 'CM%d,%d%s' % (switch, fallback, self.terminator)
        else:
            return self.terminator
			
    def charPlot(self, spaces = None, lines = None):
        """
			Move the pen the specified number of spaces and lines
			valid values are -128 to 128
			CP by itself does CR & LF
		"""
        if 'CP' in self.allowedCommands:
			if spaces and lines:
				return 'CP%d,%d%s' % (spaces, lines, self.terminator)
			else:
				return 'CP%s' % self.terminator
        else:
            return self.terminator
	
    def charSet(self, set = 0):
        if 'CS' in self.allowedCommands:
            return 'CS%d%s' % (set, self.terminator)
        else:
            return self.terminator
	
    def chordTolerance(self, type = 0):
        if 'CT' in self.allowedCommands:
            return 'CT%i%s' % (type, self.terminator)
        else:
            return self.terminator

    def curvedLineGenerator(self, n = None, inputDelay = None):
        if 'CV' in self.allowedCommands:
			if n:
				if inputDelay:
					return 'CT%d,%d%s' % (n, inputDelay, self.terminator)
				else:
					return 'CT%d%s' % (n, self.terminator)			
        else:
            return self.terminator
			
    def clearDigitizer(self):
		if 'DC' in self.allowedCommands:
			return 'DC%s' % (self.terminator)
		else:
			return self.terminator
	
    def defaultInstruction(self):
        if 'DF' in self.allowedCommands:
            return 'DF%s' % (self.terminator)
        else:
            return self.terminator
	
    def absoluteDirection(self, run = 1, rise = 0):
        if 'DI' in self.allowedCommands:
            return 'DI%d,%d%s' % (run, rise, self.terminator)
        else:
            return self.terminator

	def defineDownloadableCharacter(self):
		""" DL NOT IMPLEMENTED!!! """
		return self.terminator	
	
    def digitizePoint(self):
        if 'DP' in self.allowedCommands:
            return 'DP%s' % (self.terminator)
        else:
            return self.terminator

    def relativeDirection(self, run = 1, rise = 0):
        if 'DR' in self.allowedCommands:
            return 'DR%.4f,%.4f%s' % (run, rise, self.terminator)
        else:
            return self.terminator

	def designateCharSetIntoSlot(self):
		""" DS NOT IMPLEMENTED!!! """
		return self.terminator

    def defineLabelTerminator(self, t = chr(3)):
        if 'DT' in self.allowedCommands:
            return 'DT%c%s' % (t, self.terminator)
        else:
            return self.terminator

	def directionVertical(self, dir = 0):
		if 'DV' in self.allowedCommands:
			return 'DV%d%s' % (dir, self.terminator)
		else:
			return self.terminator

    def edgeRectAbsolute(self, x, y):
        """Draw edge rectangle at absolute position x,y."""
        if 'EA' in self.allowedCommands:
            return 'EA%.4f,%.4f%s' % (x, y, self.terminator)
        else:
            return self.terminator

	def enableCutLine(self, n):
		if 'EC' in self.allowedCommands:
			return 'EC%d%s' % (n, self.terminator)
		else:
			return self.terminator
			
	def edgePolygon(self):
		if 'EP' in self.allowedCommands:
			return 'EP%s' % self.terminator
		else:
			return self.terminator
	
    def edgeRectRelative(self, x, y):
        """Draw edge rectangle at relative position x,y."""
        if 'ER' in self.allowedCommands:
            return 'ER%.4f,%.4f%s' % (x, y, self.terminator)
        else:
            return self.terminator
            
    def extraSpace(self, spaces = 0, lines = 0):
        if 'ES' in self.allowedCommands:
            return 'ES%d,%d%s' % (spaces, lines, self.terminator)
        else:
            return self.terminator

    def edgeWedge(self, r, sa, swa, ca=5):
        """Draw the edge of a wedge, or a hedge."""
        if 'EW' in self.allowedCommands:
            return 'EW%.4f,%d,%d,%d%s' % (r, sa, swa, ca, self.terminator)
        else:
            return self.terminator

	def fillPolygon(self):
		if 'FP' in self.allowedCommands:
			return 'FP%s' % self.terminator

	def advanceFrame(self):
		if 'FR' in self.allowedCommands:
			return 'FR' + self.terminator
		else:
			return self.terminator

    def forceSelect(self, force = None, pen = None):
        """
			Set tip force for pen. 
			force range is 1-8
			pen range is 1-8
			if pen == None then all pens are set to force
		"""
        if 'FS' in self.allowedCommands:
            if force == None:
                return 'FS' + self.terminator
            elif pen:
                return 'FS%d,%d%s' % (force, pen, self.terminator)
            else:
                return 'FS%d%s' % (force, self.terminator)
        else:
            return self.terminator

    def fillType(self, type=1, space=None,  angle=0):
        """ Set fill type.
        type:
        1:  Solid (space and angle ignored)
        2:  Solid too? (space and angle ignored)
        3:  Hatching
        4:  Cross hatching
        """
		
        if 'FT' in self.allowedCommands:
            if space == None:
				return 'FT%d%s' % (type, self.terminator)
            else:
                return 'FT%d,%.4f,%d%s' % (type, space, angle, self.terminator)
        else:
            return self.terminator

	def groupCount(self, count = 0):
		""" GC NOT IMPLEMENTED!!! """
        return self.terminator
			
	def graphicsMemory(self):
		""" GM NOT IMPLEMENTED!!! """
		return self.terminator

	def groupPen(self):
		""" GP NOT IMPLEMENTED!!! """
		return self.terminator

    def inputMask(self, e = 233, s = 0, p = 0):
        """
			Set masks for Error LED, Status byte, and Positive serial poll.
			Whatever.
		"""
        if 'IM' in self.allowedCommands:
            return 'IM%d,%d,%d%s' % (e, s, p, self.terminator)
        else:
            return self.terminator

    def initialize(self):
        if 'IN' in self.allowedCommands:
            return 'IN' + self.terminator
        else:
            return self.terminator

    def inputP1P2(self, p1x = None, p1y = None, p2x = None, p2y = None):
        """Set P1 & P2 scaling points"""
        if 'IP' in self.allowedCommands:
			if p1x == None or p1y == None:
				return 'IP%s' % (self.terminator)
			elif p2x == None or p2y == None:
				return 'IP%d,%d%s' % (p1x, p1y, self.terminator)
			else:
				return 'IP%d,%d,%d,%d%s' % (p1x, p1y, p2x, p2y, self.terminator)
        else:
            return self.terminator


    def invokeCharSlant(self, slot = 0, left = None):
        if 'IV' in self.allowedCommands:
			if left:
				return 'IV%d,%d%s' % (slot, left)
			else:
				return 'IV%d%d' % (slot, self.terminator)
        else:
            return self.terminator

    def inputWindow(self, xLL = None, yLL = None, xUR = None, yUR = None):
        """Set plotting window."""
        if 'IW' in self.allowedCommands:
			if xLL == None or yLL == None or xUR == None or yUR == None:
				return 'IW%s' % (self.terminator)
			else:
				return 'IW%d,%d,%d,%d%s' % (xLL, yLL, xUR, yUR, self.terminator)
        else:
            return self.terminator

    def defineKey(self, key = None, function = None):
        if 'KY' in self.allowedCommands:
			if key:
				if function:
					return 'KY%d,%d%s' % (key, function, self.terminator)
				else:
					return 'KY%d%s' % (key, self.terminator)
			else:
				return 'KY%s' % (self.terminator)
        else:
            return self.terminator

    def label(self, text):
        """Print text 'label'."""
        if 'LB' in self.allowedCommands:
            return 'LB' + text + chr(3) + self.terminator
        else:
            return self.terminator

	def labelOrigin(self, positionNum = 1):
		if 'LO' in self.allowedCommands:
			return 'LO%d%s' % (positionNum, self.terminator)
		else:
			return self.terminator

    def lineType(self, patNum = None, patLength = 4):
        """Define line type.
        pattype can be:
        0:  plot point at given point.
        1:  .   .   .   .   .   .
        2:  __   __   __   __   __
        3:  ___ ___ ___ ___ ___
        4:  __.__.__.__.__.__.
        5:  ___ _ ___ _ ___ _ ___ _
        6:  ___ _ _ ___ _ _ ___ _ _ ___
        """
        if 'LT' in self.allowedCommands:
            if patNum == None:
				return 'LT%s' % (self.terminator)
            else:				
                return 'LT%d,%.4f%s' % (patNum, patLength, self.terminator)
        else:
            return self.terminator

	def notReady(self):
		if 'NR' in self.allowedCommands:
			return 'NR' + self.terminator
		else:
			return self.terminator

    def outputActualPosition(self):
        """
			Returns current actual position of pen.
			X, Y, P (0 = PU, 1 = PD)
		"""
        if 'OA' in self.allowedCommands:
            return 'OA%s' % (self.terminator)
        else:
            return self.terminator

    def outputCommandedPosition(self):
        """
			Returns commanded position of pen.
			X, Y, P (0 = PU, 1 = PD)
		"""
        if 'OC' in self.allowedCommands:
            return 'OC%s' % (self.terminator)
        else:
            return self.terminator

    def outputDigiPoint(self):
        """
			Returns last digitized point.
			X, Y, P (0 = PU, 1 = PD)
		"""
        if 'OD' in self.allowedCommands:
            return 'OD%s' % (self.terminator)
        else:
            return self.terminator

    def outputError(self):
        """
			Return first HP-GL error.
			#'s 0-8, excluding 4 and 7
			
			bit value	error no	meaning
			0			0			no error
			1			1			unrecognized command
			2			2			wrong num of parameters
			4			3			out-of-range parameter
			8			4			unused
			16			5			unknown character set
			32			6			position overflow
			64			7			unused
			128			8			pinch wheels raised
			
			
			NOTE: some error meanings change depending on the plotter!
		"""
        if 'OE' in self.allowedCommands:
            return 'OE%s' % (self.terminator)
        else:
            return self.terminator

    def outputFactors(self):
        """
			dog ass me.
			
			Always outputs '40,40', which means that there are 40 plotter units/mm
		"""
        if 'OF' in self.allowedCommands:
            return 'OF%s' % (self.terminator)
        else:
            return self.terminator

	def outputGroupCount(self):
		""" OG NOT IMPLEMENTED!!! """
        return self.terminator

    def outputHardClipLimits(self):
        """Return hard limits of plotter"""
        if 'OH' in self.allowedCommands:
            return 'OH%s' % (self.terminator)
        else:
            return self.terminator

    def outputID(self):
        """Get ID of plotter."""
        if 'OI' in self.allowedCommands:
            return 'OI' + self.terminator
        else:
            return self.terminator

	def outputKey(self):
		if 'OK' in self.allowedCommands:
			return 'OK' + self.terminator
		else:
			return self.terminator

	def outputLabelLength(self):
		if 'OL' in self.allowedCommands:
			return 'OL' + self.terminator
		else:
			return self.terminator

    def outputOptions(self):
        """
			Get features implemented on this plotter.
			0,1,0,0,1,0,0,0 TERM
			first 1 = pen select
			second 1 = arcs & circles
		"""
        if 'OO' in self.allowedCommands:
            return 'OO' + self.terminator
        else:
            return self.terminator

    def outputP1P2(self):
        """Get P1 & P2."""
        if 'OP' in self.allowedCommands:
            return 'OP' + self.terminator
        else:
            return self.terminator
            
    def outputStatus(self):
        """
			Return plotter status.
			
			bit value	bit position	meaning
			1			0				pen down
			2			1				P1 or P2 changed ("OP" clears)
			4			2				digitized point ready ("OD" clears)
			8			3				initialized ("OS" clears)
			16			4				ready to recieve data (always 0)
			32			5				There is an error ("OE" clears)
			64			6				unused
			128			7				unused
			
			power-on status == 24 (bits 3 & 4 set)
			
			but these may be different on different plotters...
		"""
        if 'OS' in self.allowedCommands:
            return 'OS' + self.terminator
        else:
            return self.terminator
            
	def outputCarouselType(self):
		if 'OT' in self.allowedCommands:
			return 'OT' + self.terminator
		else:
			return self.terminator

    def outputWindow(self):
        """Return xLL, yLL, xUR, yUR in plotter coords."""
        if 'OW' in self.allowedCommands:
            return 'OW' + self.terminator
        else:
            return self.terminator

    def plotAbsolute(self, coords = None):
        """
            Plot Absolute.
            coords is a tuple with any number of x,y pairs!!!
        """
        if 'PA' in self.allowedCommands:
            if coords == None:
                return 'PA%s' % (self.terminator)
            else:
                command = 'PA'
                for point in coords:
                    command += "%.4f," % point
                command = command.rstrip(',')
                return '%s%s' % (command, self.terminator)
        else:
            return self.terminator

	def printBufferedLabel(self):
		if 'PB' in self.allowedCommands:
			return 'PB' + self.terminator
		else:
			return self.terminator
			
    def penDown(self, coords = None):
        """
			Pen Down.
			coords is a tuple with any number of x,y pairs!!!
		"""
        if 'PD' in self.allowedCommands:
            if coords == None:
                return 'PD' + self.terminator
            else:
                command = 'PD'
                for point in coords:
                    command += "%.4f," % point
                command = command.rstrip(',')
                return '%s%s' % (command, self.terminator)
        else:
            return self.terminator

	def pageFeed(self, n = None):
		if 'PG' in self.allowedCommands:
			if n:
				return 'PG%d%s' % (n, self.terminator) 
			else:
				return 'PG' + self.terminator
		else:
			return self.terminator

	def plotPolygon(self, n = 0):
		if 'PM' in self.allowedCommands:
			return 'PM%d%s' % (n, self.terminator)
		else:
			return self.terminator

    def plotRelative(self, coords = None):
        """
            Plot Relative.
            coords is a tuple with any number of x,y pairs!!!
        """
        if 'PR' in self.allowedCommands:
            if coords == None:
                return 'PR%s' % (self.terminator)
            else:
                command = 'PR'
                for point in coords:
                    command += "%.4f," % point
                command = command.rstrip(',')
                return '%s%s' % (command, self.terminator)
        else:
            return self.terminator

    def paperSize(self, size = None):
        """
			Paper Size
			0-3 == B or A3 size paper
			4-127 == A or A4 size paper
			WTF?
        """
        if 'PS' in self.allowedCommands:
            if size:
                return 'PS%d%s' % (size, self.terminator)
            else:
                return 'PS' + self.terminator
        else:
            return self.terminator

	def penThickness(self, thickness = 0.3):
		"""
			Pen Thickness
			0.1mm < thickness < 5.0mm
		"""
		if 'PT' in self.allowedCommands:
			return 'PT%.4f%s' % (thickness, self.terminator)
		else:
			return self.terminator
			
    def penUp(self, coords = None):
        """
			Pen Up.
			coords is a tuple with any number of x,y pairs!!!
        """
        if 'PU' in self.allowedCommands:
            if coords == None:
                return 'PU' + self.terminator
            else:
                command = 'PU'
                for point in coords:
                    command += "%.4f," % point 
                command = command.rstrip(',')
                return '%s%s' % (command, self.terminator)
        else:
            return self.terminator			
			
    def shadeRectAbsolute(self, x, y):
        """Draw filled rectangle at absolute position x,y."""
        if 'RA' in self.allowedCommands:
            return 'RA%.4f,%.4f%s' % (x, y, self.terminator)
        else:
            return self.terminator

    def rotateCoordSystem(self, angle = 0):
        if 'RO' in self.allowedCommands:
            return 'RO%d%s' % (angle, self.terminator)
        else:
            return self.terminator

	def replot(self, n = 1):
		if 'RP' in self.allowedCommands:
			return 'RP%d%s' % (n, self.terminator)
		else:
			return self.terminator

    def shadeRectRelative(self, x, y):
        """Draw filled rectangle at relative position x,y."""
        if 'RR' in self.allowedCommands:
            return 'RR%.4f,%.4f%s' % (x, y, self.terminator)
        else:
            return self.terminator
			
    def selectAltCharSet(self):
        if 'SA' in self.allowedCommands:
            return 'SA%s' %  self.terminator
        else:
            return self.terminator			
			
    def scale(self, xMin, xMax, yMin, yMax):
        """
			NOTE: DraftMaster also has a more complex version of 'SC' that is
			not implemented yet...
        """
        if 'SC' in self.allowedCommands:
            return 'SC%d,%d,%d,%d%s' % (xMin, xMax, yMin, yMax, self.terminator)
        else:
            return self.terminator

	def selectPenGroup(self):
		""" SG NOT IMPLEMENTED!!! """
		return self.terminator

    def absCharSize(self, w = None, h = None):
        if 'SI' in self.allowedCommands:
			if w == None or h == None:
				return 'SI%s' % self.terminator
			else:
				return 'SI%.4f,%.4f%s' % (w, h, self.terminator)
        else:
            return self.terminator

    def charSlant(self, tan = 0):
        """ 
			Character Slant
			argument is tan of desired angle
			We do an autoconvert in plotter.py
        """
        if 'SL' in self.allowedCommands:
            #angle = angle * 2 * math.pi / 360.
            return 'SL%.4f%s' % (tan, self.terminator)
        else:
            return self.terminator
			
	def symbolMode(self, char = None):
		"""
			Symbol Mode.
			Plots the char at each plotted point. 
			char can be any printing ascii char, except ';'
			Calling without an argument cancels symbol mode.
		"""
        if 'SM' in self.allowedCommands:
			if char == None:
				return 'SM%s' % self.terminator
			else:
				return 'SM%c%s' % (char, self.terminator)
        else:
            return self.terminator		
	
    def selectPen(self, penNum = 0):
        if 'SP' in self.allowedCommands:
            return 'SP%d%s' % (penNum, self.terminator)
        else:
            return self.terminator

    def relCharSize(self, w = None, h = None):
        if 'SR' in self.allowedCommands:
			if w and h:
				return 'SR%.4f,%.4f%s' % (w, h, self.terminator)
			else:
				return 'SR' + self.terminator
        else:
            return self.terminator
			
    def selectStandardCharSet(self):
        if 'SS' in self.allowedCommands:
            return 'SS%s' % (self.terminator)
        else:
            return self.terminator
			
    def tickLength(self, tp = 0.5, tn = 0.5):
        """
			Length of ticks drawn wiht the XT and YT instructions
			tp: percentage of (P2y - P1y) for XT or (P2x - P1x) for YT
				Denotes portion above X-axis or to the right of the Y-axis when
				difference is positive.
			tn: same as tp except denotes portion below the X-axis and to the left
				of the Y-axis
			
			0.5 is default for both
        """
        if 'TL' in self.allowedCommands:
            return 'TL%.4f,%.4f%s' % (tp, tn, self.terminator)
        else:
            return self.terminator
			
	def userDefinedCharacter(self):
		""" this is wack, not implemented. """
		return self.terminator

	def userDefFillType(self):
		""" also wack, also not implemented. """
		return self.terminator

    def velocitySelect(self, v = None, pen = None):
        """ 
			Set pen's velocity.
			v valid range: 0.0-127.9999 (depends on plotter)
			default depends on plotter and carousel type
			pen valid range: 1-8
        """
        if 'VS' in self.allowedCommands:
            if pen == None:
                if v == None:
                    return 'VS%s' % self.terminator
                else:
                    return 'VS%d%s' % (v, self.terminator)
            else:
                return 'VS%d,%d%s' % (v, pen, self.terminator)
        else:
            return self.terminator

    def writeToDisplay(self, text):
        """ Writes up to 32 chars to LCD."""
        if 'WD' in self.allowedCommands:
            return 'WD' + text + chr(3)
        else:
            return self.terminator

    def shadeWedge(self, r, sa, swa, ca = 5):
        """shade a wedge, or a hedge."""
        if 'WG' in self.allowedCommands:
            return 'WG%.4f,%d,%d,%d%s' % (r, sa, swa, ca, self.terminator)
        else:
            return self.terminator

    def xTick(self):
        if 'XT' in self.allowedCommands:
            return 'XT%s' % self.terminator
        else:
            return self.terminator

    def yTick(self):
        if 'YT' in self.allowedCommands:
            return 'YT%s' % self.terminator
        else:
            return self.terminator	


    """
        ESCAPE commands
    """
    
    def escapePlotterOn(self):
        """
			Places the plotter in a programmed on-state.
			
			old description (from where?):
			Instructs the plotter to interpret data as HPGL and DCI instructions, 
			rather than plotting the data stream as literal text characters.
		"""
        return chr(27) + '.('
		
    def escapePlotterOff(self):
        """
			Places the plotter in a programmed off-state
		"""
        return chr(27) + '.)'	
	
	def escapteSetPlotterConfiguration(self, maxBufSize, dtrControl):
		"""
			Enables or disables hardwire handshake mode, monitor mode,
			and data transmission mode.
			
			maxBufSize: sets maximum buffer size
			dtrControl: Data Terminal Ready (CD) line contro. 
				A number in the range of 0-31
				
			WTF???
		"""
		return "%c.@[(%d);(%d)];" % (chr(27), maxBufSize, dtrControl)
	
    def escapeOutputBufferSpace(self):
        return chr(27) + '.B' 
	
    def extendedError(self):
        """
			Get RS-232-C related error message.
			0 == no error
			10-16 == error
			
			error num	meaning
			0			no i/o error
			10			output request received while still processing previous one
			11			invalid byte received after escape sequence ("ESC.")
			12			invalid byte received as part of a device control instruction
			13			parameter out of range
			14			too many parameters received
			15			framing, parity, or overrun error
			16			input buffer overflow
			
		"""
        return chr(27) + '.E'	

    def escapeXoff(self, char='19', interchar_speed=0):
        """DCI that tells the plotter what the Xoff character will be."""
        return chr(27) + '.N' + str(interchar_speed) + ';' + str(char) + ':'

    def escapeHS2(self, minbytes=81, xon='17' ):
        """Set hand shake mode 2."""
        return chr(27) + '.I' + str(minbytes) + ';' + ';' + str(xon) + ':'  

    def abortCommand(self):
        """Tells the plotter to discard commands in its buffer."""
        return chr(27) + '.K'
        
