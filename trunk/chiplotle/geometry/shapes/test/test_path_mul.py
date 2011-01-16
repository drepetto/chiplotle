from chiplotle.geometry.shapes.path import Path


def test_path_mul_01( ):
   '''A Path and a scalar can be multiplied.'''
   a = Path([(1, 2), (3, 4)])
   t = a * 2
   assert isinstance(t, Path)
   assert t is not a
   assert t == Path([(2, 4), (6, 8)])


def test_path_rmul_01( ):
   '''A scalar and a Path can be multiplied.'''
   a = Path([(1, 2), (3, 4)])
   t = 2 * a
   assert isinstance(t, Path)
   assert t is not a
   assert t == Path([(2, 4), (6, 8)])


def test_path_mul_02( ):
   '''A Path and a duple can be multiplied.'''
   a = Path([(1, 2), (3, 4)])
   t = a * (1, 2)
   assert isinstance(t, Path)
   assert t is not a
   assert t == Path([(1, 4), (3, 8)])


def test_path_rmul_02( ):
   '''A duple and a Path can be multiplied.'''
   a = Path([(1, 2), (3, 4)])
   t = (1, 2) * a
   assert isinstance(t, Path)
   assert t is not a
   assert t == Path([(1, 4), (3, 8)])

