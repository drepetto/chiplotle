from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.commands import LB, PA, ES, LO, SL, DI, DV, SI


class Label(object):
    """Text label.

    * `xy`: 2-tuple of coordinates pair for label location.
    * `text`: The actual text to be printed.
    * `charwidth`:  absolute character width in centimiters.
    * `charheight`:  absolute character height in centimiters.
    * `direction`: 2-tuple. The inclination / angle of the text:
        run (direction on x axis), rise (direction on y axis).
    * `charspace`: Factor to set spacing between characters.
        Positive separates, negatives bring together.
    * `linespace`: Factor to set spacing between lines.
        Positive separates, negatives bring together.
    * `origin`: location of label relative to pen's current location.
        Possible values:

            ====== ===== ======= =======
            .      Left  Inside  Right
            ====== ===== ======= =======
            Above    3     6      9
            Inside   2     5      8
            Below    1     4      7
            ====== ===== ======= =======

            If 10 is added to the above-mentioned location number, positions
            (except 5) will be offset towards the center by 1/2 the character
            width and 1/2 the character height.

    * `slant`: slant of characters (italic). Possible values: [0-1).
        0 is vertical, 0.5 is 45 degs., ...
    * `vertical`: Print text from left to right (False) or top down (True).
    """

    def __init__(
        self,
        text,
        charwidth=None,
        charheight=None,
        charspace=None,
        linespace=None,
        origin=1,
        slant=0,
        direction=None,
        vertical=False,
    ):

        self.text = text
        self.charwidth = charwidth
        self.charheight = charheight
        self.direction = direction
        self.charspace = charspace
        self.linespace = linespace
        self.origin = origin
        self.slant = slant
        self.vertical = vertical

    @property
    def _subcommands(self):
        result = []
        if self.direction:
            result.append(DI(*self.direction))
        else:
            result.append(DI())
        result.append(SI(width=self.charwidth, height=self.charheight))
        result.append(ES(charspace=self.charspace, linespace=self.linespace))
        result.append(LO(origin=self.origin))
        result.append(SL(tan=self.slant))
        result.append(DV(vertical=self.vertical))
        result.append(LB(self.text))

        return result

    @property
    def format(self):
        return b"".join([c.format for c in self._subcommands])


## demo
if __name__ == "__main__":
    print(Label("Hello!").format)
    print(Label("Adios!", 1, 2, direction=(1, 2)).format)
