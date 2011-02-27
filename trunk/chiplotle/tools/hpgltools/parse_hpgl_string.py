import re

def parse_hpgl_string(arg):
   '''The function takes a string `arg` of HPGL commands, parses them
   (separates them) and returns them in a list.
   '''
   if not isinstance(arg, str):
      raise TypeError('`arg` must be of type string.')

   hpgl_commands = ['AA','AF','AH','AP','AR','AS',
      'BF','BL',
      'CA','CC','CI','CM','CP','CS','CT','CV',
      'DC','DF','DI','DP','DR','DS','DT','DV', #DL
      'EA','EC','EP','ER','ES','EW',
      'FP','FR','FS','FT',
      'GC', #GM GP
      'IM','IN','IP','IV','IW',
      'KY',
      'LB','LO','LT',
      'NR',
      'OA','OC','OD','OE','OF','OG','OH','OI','OK','OL','OO','OP','OS','OT','OW',
      'PA','PB','PD','PG','PM','PR','PS','PT','PU',
      'RA','RO','RR',
      'SA','SC','SI','SL','SM','SP','SR','SS', #SG
      'TL',
      #'UC', UF
      'VS',
      'WD','WG',
      'XT',
      'YT']
   ## TODO: Add all the supported escape (DCI) commands.
   dci_commands = ['\x1b\.\(', '\x1b\.Y']

   # NOTE: added '-' to hpgl_patter because we were barfing on strings like
   # 'PA1.99,-5.00;' -- the ,- construction wasn't being parsed correctly.
   # Don't understand why normal negative integers were being parsed
   # correctly though...
   hpgl_pattern = '[-0-9.,]*|'.join(hpgl_commands)
   dci_pattern = '[0-9.;]*|'.join(dci_commands)
   pattern = hpgl_pattern + "|" + dci_pattern
   ## this assumes that the re will find each and every hpgl command
   ## with the pattern. Any command not matched will effectively be
   ## romoved... we don't want that. 
   result = re.findall(pattern, arg) 
   return result
