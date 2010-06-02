from chiplotle import *
import os

def test_import_hpgl_file_01( ):
   path = os.path.dirname(os.path.abspath(__file__))
   t = io.import_hpgl_file(os.path.join(path, 'hpgl_import_test_file.hpgl'))

   assert t[0].format == 'IN;'
   assert t[1].format == 'IP0,0,8128,8128;'
   assert t[2].format == 'SC0,10000,0,10000;'
   assert t[3].format == 'SP1;'
   assert t[4].format == 'LT;'
   assert t[5].format == 'PM0;'
   assert t[6].format == 'PU;'
   assert t[7].format == 'PA0,0;'
   assert t[8].format == 'PD;'
   assert t[9].format == 'PA10,0,10,10,0,10,0,0;'
   assert t[10].format == 'PM2;'
   assert t[11].format == 'PU;'
   assert t[12].format == 'FT2;'
   assert t[13].format == 'FP;'
   assert t[14].format == 'EP;'
   assert t[15].format == 'SP0;'
