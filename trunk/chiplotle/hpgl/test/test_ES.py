from chiplotle.hpgl.commands import ES

def test_ES_01( ):
   t = ES( )
   assert t.charspace == None
   assert t.linespace == None
   assert t.format == 'ES;'
   

def test_ES_02( ):
   t = ES(0)
   assert t.charspace == 0
   assert t.linespace == None
   assert t.format == 'ES0.00;'

def test_ES_03( ):
   t = ES(1)
   assert t.charspace == 1
   assert t.linespace == None
   assert t.format == 'ES1.00;'

def test_ES_04( ):
   t = ES(1, 0)
   assert t.charspace == 1
   assert t.linespace == 0
   assert t.format == 'ES1.00,0.00;'

def test_ES_04( ):
   t = ES(1, 1)
   assert t.charspace == 1
   assert t.linespace == 1
   assert t.format == 'ES1.00,1.00;'

