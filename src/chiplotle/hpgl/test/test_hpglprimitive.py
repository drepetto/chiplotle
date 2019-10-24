from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import PU
from chiplotle.hpgl.abstract.hpglprimitive import _HPGLPrimitive


def teardown_module(module):
    ## Reset terminator back to default ';' so that future
    ## tests don't fail.
    _HPGLPrimitive._terminator = b";"

def test_hpglprimitive_terminator_01():
    """the _HPGLPrimitive class has a _terminator attribute that defines
    the terminator for HPGL commands. The default is `;`."""

    assert _HPGLPrimitive._terminator == b";"

    t = PU()
    assert t.format == b"PU;"

    _HPGLPrimitive._terminator = b"@"
    assert t.format == b"PU@"

    t = PU()
    assert t.format == b"PU@"
