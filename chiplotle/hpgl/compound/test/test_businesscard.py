from chiplotle import *

#def test_businesscard_01( ):
#   c = Cube((0, 200), 500, 500, 500,  rotation=(1.1, 2.9, 2.3))
#   t = BusinessCard((0, 0), c, [])


def test_buisnesscard_scalable_01( ):
   assert BusinessCard._scalable == ['xy', 'width', 'height']
