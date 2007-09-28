
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""





"""
    chiplotle implementation of many HPGL commands.

"""

TERMINATOR = ';'
        

"""
    HPGL translations
"""

def arcAbsolute(x, y, aa, ca = 5):
    return 'AA%d,%d,%d,%d%s' % (x, y, aa, ca, TERMINATOR)

def advanceFullPage():
    return 'AF%s' % (TERMINATOR)

def advanceHalfPage():
    return 'AH%s' % (TERMINATOR)

def automaticPen(p = None):
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
    if p:
        return 'AP%d%s' % (p, TERMINATOR)
    else:
        return 'AP' + TERMINATOR

def arcRelative(x, y, aa, ca = 5):
    return 'AR%d,%d,%d,%d%s' % (x, y, aa, ca, TERMINATOR)

def accelSelect(accel = None, pen = None):
    """
        Acceleration Select
        Can be set per-pen or for all pens at once.

        default on 7550: 6
        default on DM: 4
    """
    if accel:
        if pen:
            return 'AS%d,%d%s' % (accel, pen, TERMINATOR)
        else:
            return 'AS%d%s' % (accel, TERMINATOR)					
    else:
        return 'AS' + TERMINATOR

def bufferPlot():
    return 'BF%s' % (TERMINATOR)

def bufferLabel(text = None):
    """
        Stores first 150 chars of text in buffer for later printing
        and label length measurements.
    """
    if text == None:
        return 'BL%s' % (TERMINATOR)
    else:
        return 'BL' + text + chr(3) + TERMINATOR

def altCharSet(n = 0):
    return 'CA%d%s' % (n, TERMINATOR)

def charChordAngle(angle = 5):
    return 'CC%d%s' % (angle, TERMINATOR)

def circle(r, ca = 5):
    return 'CI%d,%d%s' % (r, ca, TERMINATOR)

def charSelectionMode(switch = 0, fallback = 0):
    return 'CM%d,%d%s' % (switch, fallback, TERMINATOR)
        
def charPlot(spaces = None, lines = None):
    """
        Move the pen the specified number of spaces and lines
        valid values are -128 to 128
        CP by itself does CR & LF
    """
    if spaces and lines:
        return 'CP%d,%d%s' % (spaces, lines, TERMINATOR)
    else:
        return 'CP%s' % TERMINATOR

def charSet(set = 0):
    return 'CS%d%s' % (set, TERMINATOR)

def chordTolerance(type = 0):
    return 'CT%i%s' % (type, TERMINATOR)

def curvedLineGenerator(n = None, inputDelay = None):
    if n:
        if inputDelay:
            return 'CT%d,%d%s' % (n, inputDelay, TERMINATOR)
        else:
            return 'CT%d%s' % (n, TERMINATOR)			
        
def clearDigitizer():
    return 'DC%s' % (TERMINATOR)

def defaultInstruction():
    return 'DF%s' % (TERMINATOR)

def absoluteDirection(run = 1, rise = 0):
    return 'DI%d,%d%s' % (run, rise, TERMINATOR)

def defineDownloadableCharacter():
    """ DL NOT IMPLEMENTED!!! """
    return TERMINATOR	

def digitizePoint():
    return 'DP%s' % (TERMINATOR)

def relativeDirection(run = 1, rise = 0):
    return 'DR%.4f,%.4f%s' % (run, rise, TERMINATOR)

def designateCharSetIntoSlot():
    """ DS NOT IMPLEMENTED!!! """
    return TERMINATOR

def defineLabelTerminator(t = chr(3)):
    return 'DT%c%s' % (t, TERMINATOR)

def directionVertical(dir = 0):
    return 'DV%d%s' % (dir, TERMINATOR)

def edgeRectAbsolute(x, y):
    """Draw edge rectangle at absolute position x,y."""
    return 'EA%.4f,%.4f%s' % (x, y, TERMINATOR)

def enableCutLine(n):
    return 'EC%d%s' % (n, TERMINATOR)
        
def edgePolygon():
    return 'EP%s' % TERMINATOR

def edgeRectRelative(x, y):
    """Draw edge rectangle at relative position x,y."""
    return 'ER%.4f,%.4f%s' % (x, y, TERMINATOR)
        
def extraSpace(spaces = 0, lines = 0):
    return 'ES%d,%d%s' % (spaces, lines, TERMINATOR)

def edgeWedge(r, sa, swa, ca=5):
    """Draw the edge of a wedge, or a hedge."""
    return 'EW%.4f,%d,%d,%d%s' % (r, sa, swa, ca, TERMINATOR)

def fillPolygon():
    return 'FP%s' % TERMINATOR

def advanceFrame():
    return 'FR' + TERMINATOR

def forceSelect(force = None, pen = None):
    """
        Set tip force for pen. 
        force range is 1-8
        pen range is 1-8
        if pen == None then all pens are set to force
    """
    if force == None:
        return 'FS' + TERMINATOR
    elif pen:
        return 'FS%d,%d%s' % (force, pen, TERMINATOR)
    else:
        return 'FS%d%s' % (force, TERMINATOR)

def fillType(type=1, space=None,  angle=0):
    """ Set fill type.
    type:
    1:  Solid (space and angle ignored)
    2:  Solid too? (space and angle ignored)
    3:  Hatching
    4:  Cross hatching
    """
    
    if space == None:
        return 'FT%d%s' % (type, TERMINATOR)
    else:
        return 'FT%d,%.4f,%d%s' % (type, space, angle, TERMINATOR)

def groupCount(count = 0):
    """ GC NOT IMPLEMENTED!!! """
    return TERMINATOR
        
def graphicsMemory():
    """ GM NOT IMPLEMENTED!!! """
    return TERMINATOR

def groupPen():
    """ GP NOT IMPLEMENTED!!! """
    return TERMINATOR

def inputMask(e = 233, s = 0, p = 0):
    """
        Set masks for Error LED, Status byte, and Positive serial poll.
        Whatever.
    """
    return 'IM%d,%d,%d%s' % (e, s, p, TERMINATOR)

def initialize():
    return 'IN' + TERMINATOR

def inputP1P2(p1x = None, p1y = None, p2x = None, p2y = None):
    """Set P1 & P2 scaling points"""
    if p1x == None or p1y == None:
        return 'IP%s' % (TERMINATOR)
    elif p2x == None or p2y == None:
        return 'IP%d,%d%s' % (p1x, p1y, TERMINATOR)
    else:
        return 'IP%d,%d,%d,%d%s' % (p1x, p1y, p2x, p2y, TERMINATOR)


def invokeCharSlant(slot = 0, left = None):
    if left:
        return 'IV%d,%d%s' % (slot, left)
    else:
        return 'IV%d%d' % (slot, TERMINATOR)

def inputWindow(xLL = None, yLL = None, xUR = None, yUR = None):
    """Set plotting window."""
    if xLL == None or yLL == None or xUR == None or yUR == None:
        return 'IW%s' % (TERMINATOR)
    else:
        return 'IW%d,%d,%d,%d%s' % (xLL, yLL, xUR, yUR, TERMINATOR)

def defineKey(key = None, function = None):
    if key:
        if function:
            return 'KY%d,%d%s' % (key, function, TERMINATOR)
        else:
            return 'KY%d%s' % (key, TERMINATOR)
    else:
        return 'KY%s' % (TERMINATOR)

def label(text):
    """Print text 'label'."""
    return 'LB' + text + chr(3) + TERMINATOR

def labelOrigin(positionNum = 1):
    return 'LO%d%s' % (positionNum, TERMINATOR)

def lineType(patNum = None, patLength = 4):
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
    if patNum == None:
        return 'LT%s' % (TERMINATOR)
    else:				
        return 'LT%d,%.4f%s' % (patNum, patLength, TERMINATOR)

def notReady():
    return 'NR' + TERMINATOR

def outputActualPosition():
    """
        Returns current actual position of pen.
        X, Y, P (0 = PU, 1 = PD)
    """
    return 'OA%s' % (TERMINATOR)

def outputCommandedPosition():
    """
        Returns commanded position of pen.
        X, Y, P (0 = PU, 1 = PD)
    """
    return 'OC%s' % (TERMINATOR)

def outputDigiPoint():
    """
        Returns last digitized point.
        X, Y, P (0 = PU, 1 = PD)
    """
    return 'OD%s' % (TERMINATOR)

def outputError():
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
    return 'OE%s' % (TERMINATOR)

def outputFactors():
    """
        dog ass me.
        
        Always outputs '40,40', which means that there are 40 plotter units/mm
    """
    return 'OF%s' % (TERMINATOR)

def outputGroupCount():
    """ OG NOT IMPLEMENTED!!! """
    return TERMINATOR

def outputHardClipLimits():
    """Return hard limits of plotter"""
    return 'OH%s' % (TERMINATOR)

def outputID():
    """Get ID of plotter."""
    return 'OI' + TERMINATOR

def outputKey():
    return 'OK' + TERMINATOR

def outputLabelLength():
    return 'OL' + TERMINATOR

def outputOptions():
    """
        Get features implemented on this plotter.
        0,1,0,0,1,0,0,0 TERM
        first 1 = pen select
        second 1 = arcs & circles
    """
    return 'OO' + TERMINATOR

def outputP1P2():
    """Get P1 & P2."""
    return 'OP' + TERMINATOR
        
def outputStatus():
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
    return 'OS' + TERMINATOR
        
def outputCarouselType():
    return 'OT' + TERMINATOR

def outputWindow():
    """Return xLL, yLL, xUR, yUR in plotter coords."""
    return 'OW' + TERMINATOR

def plotAbsolute(coords = None):
    """
        Plot Absolute.
        coords is a tuple with any number of x,y pairs!!!
    """
    if coords == None:
        return 'PA%s' % (TERMINATOR)
    else:
        command = 'PA'
        for point in coords:
            command += "%.4f," % point
        command = command.rstrip(',')
        return '%s%s' % (command, TERMINATOR)

def printBufferedLabel():
    return 'PB' + TERMINATOR
        
def penDown(coords = None):
    """
        Pen Down.
        coords is a tuple with any number of x,y pairs!!!
    """
    if coords == None:
        return 'PD' + TERMINATOR
    else:
        command = 'PD'
        for point in coords:
            command += "%.4f," % point
        command = command.rstrip(',')
        return '%s%s' % (command, TERMINATOR)

def pageFeed(n = None):
    if n:
        return 'PG%d%s' % (n, TERMINATOR) 
    else:
        return 'PG' + TERMINATOR

def plotPolygon(n = 0):
    return 'PM%d%s' % (n, TERMINATOR)

def plotRelative(coords = None):
    """
        Plot Relative.
        coords is a tuple with any number of x,y pairs!!!
    """
    if coords == None:
        return 'PR%s' % (TERMINATOR)
    else:
        command = 'PR'
        for point in coords:
            command += "%.4f," % point
        command = command.rstrip(',')
        return '%s%s' % (command, TERMINATOR)

def paperSize(size = None):
    """
        Paper Size
        0-3 == B or A3 size paper
        4-127 == A or A4 size paper
        WTF?
    """
    if size:
        return 'PS%d%s' % (size, TERMINATOR)
    else:
        return 'PS' + TERMINATOR

def penThickness(thickness = 0.3):
    """
        Pen Thickness
        0.1mm < thickness < 5.0mm
    """
    return 'PT%.4f%s' % (thickness, TERMINATOR)
        
def penUp(coords = None):
    """
        Pen Up.
        coords is a tuple with any number of x,y pairs!!!
    """
    if coords == None:
        return 'PU' + TERMINATOR
    else:
        command = 'PU'
        for point in coords:
            command += "%.4f," % point 
        command = command.rstrip(',')
        return '%s%s' % (command, TERMINATOR)
        
def shadeRectAbsolute(x, y):
    """Draw filled rectangle at absolute position x,y."""
    return 'RA%.4f,%.4f%s' % (x, y, TERMINATOR)

def rotateCoordSystem(angle = 0):
    return 'RO%d%s' % (angle, TERMINATOR)

def replot(n = 1):
    return 'RP%d%s' % (n, TERMINATOR)

def shadeRectRelative(x, y):
    """Draw filled rectangle at relative position x,y."""
    return 'RR%.4f,%.4f%s' % (x, y, TERMINATOR)
        
def selectAltCharSet():
    return 'SA%s' %  TERMINATOR
        
def scale(xMin, xMax, yMin, yMax):
    """
        NOTE: DraftMaster also has a more complex version of 'SC' that is
        not implemented yet...
    """
    return 'SC%d,%d,%d,%d%s' % (xMin, xMax, yMin, yMax, TERMINATOR)

def selectPenGroup():
    """ SG NOT IMPLEMENTED!!! """
    return TERMINATOR

def absCharSize(w = None, h = None):
    if w == None or h == None:
        return 'SI%s' % TERMINATOR
    else:
        return 'SI%.4f,%.4f%s' % (w, h, TERMINATOR)

def charSlant(tan = 0):
    """ 
        Character Slant
        argument is tan of desired angle
        We do an autoconvert in plotter.py
    """
    return 'SL%.4f%s' % (tan, TERMINATOR)
        
def symbolMode(char = None):
    """
        Symbol Mode.
        Plots the char at each plotted point. 
        char can be any printing ascii char, except ';'
        Calling without an argument cancels symbol mode.
    """
    if char == None:
        return 'SM%s' % TERMINATOR
    else:
        return 'SM%c%s' % (char, TERMINATOR)

def selectPen(penNum = 0):
    return 'SP%d%s' % (penNum, TERMINATOR)

def relCharSize(w = None, h = None):
    if w and h:
        return 'SR%.4f,%.4f%s' % (w, h, TERMINATOR)
    else:
        return 'SR' + TERMINATOR
        
def selectStandardCharSet():
    return 'SS%s' % (TERMINATOR)
        
def tickLength(tp = 0.5, tn = 0.5):
    """
        Length of ticks drawn wiht the XT and YT instructions
        tp: percentage of (P2y - P1y) for XT or (P2x - P1x) for YT
            Denotes portion above X-axis or to the right of the Y-axis when
            difference is positive.
        tn: same as tp except denotes portion below the X-axis and to the left
            of the Y-axis
        
        0.5 is default for both
    """
    return 'TL%.4f,%.4f%s' % (tp, tn, TERMINATOR)
        
def userDefinedCharacter():
    """ this is wack, not implemented. """
    return TERMINATOR

def userDefFillType():
    """ also wack, also not implemented. """
    return TERMINATOR

def velocitySelect(v = None, pen = None):
    """ 
        Set pen's velocity.
        v valid range: 0.0-127.9999 (depends on plotter)
        default depends on plotter and carousel type
        pen valid range: 1-8
    """
    if pen == None:
        if v == None:
            return 'VS%s' % TERMINATOR
        else:
            return 'VS%d%s' % (v, TERMINATOR)
    else:
        return 'VS%d,%d%s' % (v, pen, TERMINATOR)

def writeToDisplay(text):
    """ Writes up to 32 chars to LCD."""
    return 'WD' + text + chr(3)

def shadeWedge(r, sa, swa, ca = 5):
    """shade a wedge, or a hedge."""
    return 'WG%.4f,%d,%d,%d%s' % (r, sa, swa, ca, TERMINATOR)

def xTick():
    return 'XT%s' % TERMINATOR

def yTick():
    return 'YT%s' % TERMINATOR


"""
    ESCAPE commands
"""

def escapePlotterOn():
    """
        Places the plotter in a programmed on-state.
        
        old description (from where?):
        Instructs the plotter to interpret data as HPGL and DCI instructions, 
        rather than plotting the data stream as literal text characters.
    """
    return chr(27) + '.('
    
def escapePlotterOff():
    """
        Places the plotter in a programmed off-state
    """
    return chr(27) + '.)'	

def escapteSetPlotterConfiguration(maxBufSize, dtrControl):
    """
        Enables or disables hardwire handshake mode, monitor mode,
        and data transmission mode.
        
        maxBufSize: sets maximum buffer size
        dtrControl: Data Terminal Ready (CD) line contro. 
            A number in the range of 0-31
            
        WTF???
    """
    return "%c.@[(%d);(%d)];" % (chr(27), maxBufSize, dtrControl)

def escapeOutputBufferSpace():
    return chr(27) + '.B' 

def extendedError():
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

def escapeXoff(char='19', interchar_speed=0):
    """DCI that tells the plotter what the Xoff character will be."""
    return chr(27) + '.N' + str(interchar_speed) + ';' + str(char) + ':'

def escapeHS2(minbytes=81, xon='17' ):
    """Set hand shake mode 2."""
    return chr(27) + '.I' + str(minbytes) + ';' + ';' + str(xon) + ':'  

def abortCommand():
    """Tells the plotter to discard commands in its buffer."""
    return chr(27) + '.K'
    
