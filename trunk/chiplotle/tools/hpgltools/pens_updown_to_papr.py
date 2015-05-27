from chiplotle.hpgl.commands import PA, PR, PU, PD
from chiplotle.geometry.core.coordinate import Coordinate
import copy

def pens_updown_to_papr(lst):
    '''Converts all PU((x1, y1, x2, y2) and PD(x1, y1, x2, y2) found in `lst`
    into (PU( ), PA(x1, y1, x2, y2)) pair sequences.
    The function removes the coordinates from PU and PD and places them in
    PR or PA, whatever was last found in lst prior to a PU or PD.'''

    if not isinstance(lst, (list, tuple)):
        raise TypeError('`lst` argument must be a list or tuple.')

    result = [ ]
    last_move = None
    
    for e in lst:
        if isinstance(e, (PU, PD)):
            if len(e.xy) > 0:
                if last_move is None:
                    msg = "*** WARNING: %s with coordinates found without prior PA or PR. PA assumed." % e
                    print(msg)
                    last_move = PA( )

                new_move = None
                
                if isinstance(last_move, PA):
                    new_move = PA()
                elif isinstance(last_move, PR):
                    new_move = PR()
                    
                new_move.xy = e.xy
                
                up_down_command = None
                if isinstance(e, PU):
                    up_down_command = PU( )
                elif isinstance(e, PD):
                    up_down_command = PD( )
                
                result.append(up_down_command)
                result.append(new_move)
                
                last_move = new_move
            else:
                result.append(e)
        else:
            if isinstance(e, PR):
                last_move = PR( )
            elif isinstance(e, PA):
                last_move = PA( )
            result.append(e)

    return result

