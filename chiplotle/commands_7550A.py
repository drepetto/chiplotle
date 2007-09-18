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
	commands_7550A.py
	provides info on commands supported by the HP 7550A 8 pen plotter
"""

plotterType = "7550A"

# Only these commands will be sent to the plotter. All other will be eaten. Burp.
allowedHPGLCommands = tuple(['AA','AF','AH','AP','AR','BF','BL','CA','CC','CI',
    'CM','CP','CS','CT','CV','DC','DF','DI','DL','DP','DR','DS','DT','EA','EP',
    'ER','ES','EW','FP','FS','FT','GC','IM','IN','IP','IV','IW','KY','LB','LO',
    'LT','NR','OA','OC','OD','OE','OF','OG','OH','OI','OK','OL','OO','OP','OS',
    'OT','OW','PA','PB','PD','PG','PM','PR','PT','PU','RA','RO','RP','RR','SA',
    'SC','SI','SL','SM','SP','SR','SS','TL','UC','UF','VS','WD','WG','XT','YT'])

# If these commands appear at the beginning of a line the entire line will be eaten.
disallowedLinePrefixes = tuple(['PW.'])

