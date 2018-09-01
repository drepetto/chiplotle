from chiplotle.hpgl.label import Label


def test_Label_text_only():

    label = Label("hello")
    assert label.format == b"DI;SI;ES;LO1;SL0.0000;DV0;LBhello\x03;"
