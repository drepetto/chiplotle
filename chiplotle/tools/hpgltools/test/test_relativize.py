from chiplotle import *
from chiplotle.hpgl.commands import *
from chiplotle.tools.hpgltools import relativize

def test_relativize_01( ):
   '''A sequence or PAs is converted into a sequence or PRs.'''
   t = [PA([(1, 1)]), PA([(2, 2)]), PA([(3, 2)])]
   r = relativize(t)

   'r = [PR((1, 1)), PR((1, 0))]'
   assert len(r) == len(t) - 1
   assert isinstance(r[0], PR)
   assert isinstance(r[1], PR)
   assert r[0].xy == CoordinateArray([(1, 1)])
   assert r[1].xy == CoordinateArray([(1, 0)])


def test_relativize_02( ):
   '''Long PAs are converted to long PRs.'''
   t = [PA([(1, 1), (2, 3), (3, 2)])]
   r = relativize(t)

   'r = [PR([(1, 2), (1, -1)])]'
   assert len(r) == 1
   assert isinstance(r[0], PR)
   assert r[0].xy == CoordinateArray([(1, 2), (1, -1)])


def test_relativize_03( ):
   '''Long PAs are converted to long PRs.'''
   t = [PA([(3, 2)]), PA([(1, 1), (2, 3), (3, 2)])]
   r = relativize(t)

   'r = [PR(-2, -1), PR([(1, 2), (1, -1)])]'
   assert len(r) == 2
   assert isinstance(r[0], PR)
   assert isinstance(r[1], PR)
   assert r[0].xy == CoordinateArray([(-2, -1)])
   assert r[1].xy == CoordinateArray([(1, 2), (1, -1)])


def test_relativize_04( ):
   '''PUs and PDs are left alone.'''
   t = [PA([(1, 1)]), PU([(2, 2)]), PU([(3, 2)])]
   r = relativize(t)

   'r = [PU((2, 2)), PU((3, 2))]'
   assert len(r) == 2
   assert isinstance(r[0], PU)
   assert isinstance(r[1], PU)
   assert r[0].xy == CoordinateArray([(2, 2)])
   assert r[1].xy == CoordinateArray([(3, 2)])


def test_relativize_05( ):
   '''PUs and PDs are left alone.'''
   t = [PA([(1, 1)]), PR([(2, 1)]), PU([(2, 2)]), PU([(3, 2)])]
   r = relativize(t)

   'r = [PR((2, 1)), PU((2, 2)), PU((3, 2))]'
   assert len(r) == 3
   assert isinstance(r[0], PR)
   assert isinstance(r[1], PU)
   assert isinstance(r[2], PU)
   assert r[0].xy == CoordinateArray([(2, 1)])
   assert r[1].xy == CoordinateArray([(2, 2)])
   assert r[2].xy == CoordinateArray([(3, 2)])


def test_relativize_06( ):
   '''RAs are converted into RRs.'''
   t = [PR([(1, 2)]), RA((3, 3))]
   r = relativize(t)

   '[PR((1, 2)), RR((2, 1))]'
   assert len(r) == 2
   assert isinstance(r[0], PR)
   assert isinstance(r[1], RR)
   assert r[0].xy == CoordinateArray([(1, 2)])
   assert r[1].xy == Coordinate(2, 1)
