from chiplotle.hpgl.commands import FS

def test_FS_01( ):
   '''Empty initialization.'''
   t = FS( )
   assert t.force is None
   assert t.pen is None
   assert t.format == 'FS;'


def test_FS_02( ):
   '''Initialize forceocity.'''
   t = FS(1)
   assert t.force == 1
   assert t.pen is None
   assert t.format == 'FS1;'


def test_FS_03( ):
   '''Initialize forceocity and pen.'''
   t = FS(1, 2)
   assert t.force == 1
   assert t.pen == 2
   assert t.format == 'FS1,2;'


def test_FS_03( ):
   '''Setting force to None formats correctly.'''
   t = FS(1, 2)
   t.force = None
   assert t.format == 'FS;'
