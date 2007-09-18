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


"""
	commands_dxy-1300.py
	provides info on commands supported by the Roland DXY-1300 8 pen plotter
"""

plotterType = "DXY-1300"

# Only these commands will be sent to the plotter. All other will be eaten. Burp.
allowedHPGLCommands = tuple(['AA','AR','CA','CI','CP','CS','DC','DF','DI','DP','DR','DT','EA','ER','EW','FT','IM','IN',
    'IP','IW','LB','LT','OA','OC','OD','OE','OF','OH','OI','OO','OP','OS','OW','PA','PU','PD','PR','PS','PT','RA',
    'RO','RR','SA','SC','SI','SL','SM','SP','SR','SS','TL','UC','VS','WG','XT','YT'])
	
# If these commands appear at the beginning of a line the entire line will be eaten.
disallowedLinePrefixes = tuple(['PW0.'])

