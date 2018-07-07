from chiplotle import *
import os

import pytest

@pytest.mark.skip(reason="should check that h2pxx is installed")
def test_01():
    circ      = shapes.circle(100)
    filename = 'circle'
    io.export(circ, filename, 'png')

    assert os.path.exists(filename + '.png')

    os.remove(filename + '.png')
