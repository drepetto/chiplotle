from chiplotle.hpgl.commands import LT


def test_hpgl_primitive_repr():
    command = LT(pattern=6, length=5)
    print(repr(command))
    assert repr(command) == "LT(length=5, pattern=6)"