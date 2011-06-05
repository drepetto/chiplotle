from chiplotle.hpgl.commands import WG

def test_WG_01( ):

   t = WG(10, 0, 90)

   assert t.radius == 10
   assert t.startangle == 0
   assert t.sweepangle == 90
   assert t.chordangle is None
   assert t.format == 'WG10.00,0.00,90.00;'


def test_WG_02( ):

   t = WG(10, 0, 90, 4)

   assert t.radius == 10
   assert t.startangle == 0
   assert t.sweepangle == 90
   assert t.chordangle == 4
   assert t.format == 'WG10.00,0.00,90.00,4.00;'

