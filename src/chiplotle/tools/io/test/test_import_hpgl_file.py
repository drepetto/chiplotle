from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle import *
import os


def test_import_hpgl_file_01():
    path = os.path.dirname(os.path.abspath(__file__))
    t = io.import_hpgl_file(os.path.join(path, "hpgl_import_test_file.hpgl"))

    assert t[0].format == b"IN;"
    assert t[1].format == b"IP0,0,8128,8128;"
    assert t[2].format == b"SC0,10000,0,10000;"
    assert t[3].format == b"SP1;"
    assert t[4].format == b"LT;"
    assert t[5].format == b"PM0;"
    assert t[6].format == b"PU;"
    assert t[7].format == b"PA0,0;"
    assert t[8].format == b"PD;"
    assert t[9].format == b"PA10,0,10,10,0,10,0,0;"
    assert t[10].format == b"PM2;"
    assert t[11].format == b"PU;"
    assert t[12].format == b"FT2;"
    assert t[13].format == b"FP;"
    assert t[14].format == b"EP;"
    assert t[15].format == b"SP0;"
