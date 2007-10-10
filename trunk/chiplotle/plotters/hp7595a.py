
"""
 *  This file is part of chiplotle.
 *
 *  http://music.columbia.edu/cmc/chiplotle
"""

from plotter import Plotter

class HP7595A(Plotter):
    def __init__(self, ser, **kwargs):
        
        Plotter.__init__(self, ser, **kwargs)
        self.type = "HP7595A"

        self.allowedHPGLCommands = tuple(['\x1b.', 'AA','AF','AH','AP','AR','AS','BF','BL','CA','CC','CI',
        'CM','CP','CS','CT','CV','DC','DF','DI','DL','DP','DR','DS','DT','EA','EC','EP',
        'ER','ES','EW','FP','FR','FS','FT','GC','GM','GP','IC','IM','IN','IP','IV','IW',
        'KY','LB','LO','LT','NR','OA','OB','OC','OD','OE','OF','OG','OH','OI','OK','OL',
        'OO','OP','OS','OT','OW','PA','PB','PD','PG','PM','PR','PT','PU','RA','RL','RO',
        'RP','RR','SA','SC','SG','SI','SL','SM','SP','SR','SS','TL','UC','UF','VA','VN',
        'VS','WD','WG','XT','YT'])

        self.allowedHPGL2Commands = tuple(['\x1b.', 'AA','AC','AD','AR','AT','BJ','BP','CF','CI','CP','CT',
        'DC','DF','DI','DL','DP','DR','DT','DV','EA','EC','EJ','EP','ER','ES','EW','FP',
        'FR','FT','IN','IP','IR','IW','LA','LB','LO','LT','MC','MG','MT','NR','OD','OE',
        'OH','OI','OP','OS','PA','PB','PD','PE','PF','PG','PR','PS','PT','PU','PW','RA',
        'RF','RO','RP','RR','RT','SA','SC','SD','SI','SL','SM','SP','SR','SS','ST','TD',
        'UL','WG','WU'])

