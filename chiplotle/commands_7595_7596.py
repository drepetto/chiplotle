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
	commands_7596A.py
	provides info on commands supported by the HP 7550A 8 pen plotter
"""

plotterType = "7596A"

# Only these commands will be sent to the plotter. All other will be eaten. Burp.
allowedHPGLCommands = tuple(['AA','AF','AH','AP','AR','AS','BF','BL','CA','CC','CI',
    'CM','CP','CS','CT','CV','DC','DF','DI','DL','DP','DR','DS','DT','EA','EC','EP',
    'ER','ES','EW','FP','FR','FS','FT','GC','GM','GP','IC','IM','IN','IP','IV','IW',
    'KY','LB','LO','LT','NR','OA','OB','OC','OD','OE','OF','OG','OH','OI','OK','OL',
    'OO','OP','OS','OT','OW','PA','PB','PD','PG','PM','PR','PT','PU','RA','RL','RO',
    'RP','RR','SA','SC','SG','SI','SL','SM','SP','SR','SS','TL','UC','UF','VA','VN',
    'VS','WD','WG','XT','YT'])

allowedHPGL2Commands = tuple(['AA','AC','AD','AR','AT','BJ','BP','CF','CI','CP','CT',
    'DC','DF','DI','DL','DP','DR','DT','DV','EA','EC','EJ','EP','ER','ES','EW','FP',
    'FR','FT','IN','IP','IR','IW','LA','LB','LO','LT','MC','MG','MT','NR','OD','OE',
    'OH','OI','OP','OS','PA','PB','PD','PE','PF','PG','PR','PS','PT','PU','PW','RA',
    'RF','RO','RP','RR','RT','SA','SC','SD','SI','SL','SM','SP','SR','SS','ST','TD',
    'UL','WG','WU'])

# If these commands appear at the beginning of a line the entire line will be eaten.
disallowedLinePrefixes = tuple(['PW.'])

