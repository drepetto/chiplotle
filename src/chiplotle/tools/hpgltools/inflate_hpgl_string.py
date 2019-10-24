from __future__ import print_function
from __future__ import unicode_literals
from __future__ import division
from __future__ import absolute_import
from future import standard_library
from six import string_types

standard_library.install_aliases()
# WARNING: Do not remove the line below, it is not dead code, it is needed for inflate_hpgl_string
# which uses `eval` to construct the correct HPGL command.
from chiplotle.hpgl import commands as hpgl  # NOQA
from chiplotle.tools.hpgltools.parse_hpgl_string import parse_hpgl_string
from chiplotle.tools.logtools.apply_logger import apply_logger
from chiplotle.tools.iterabletools.flat_list_to_pairs import flat_list_to_pairs


def inflate_hpgl_string(string, filter_commands=None):
    """Reads a string or bytes and "inflates" it by creating
    Chiplotle-HPGL class instances of the found HPGL commands.

    Example::

        chiplotle> sp = inflate_hpgl_string('SP1;')
        chiplotle> sp
        [SP(1)]

    Example::

        chiplotle> move = inflate_hpgl_string('IN;SP1;PA10,10;', ['IN'])
        chiplotle> move
        [SP(1), PA((10, 10))]
    """

    filter_commands = filter_commands or []

    if not isinstance(string, (string_types, bytes)):
        raise TypeError("`string` must be a string or bytes")
    if not isinstance(filter_commands, (list, tuple)):
        msg = "`filter_commands` must be a list of string HPGL commands."
        raise TypeError(msg)

    if isinstance(string, bytes):
        string = string.decode("ascii")

    _unsupported_commands = ("PW", "PC", "LA", "WU", "BP")
    commands = parse_hpgl_string(string)
    result = []
    for command in commands:
        if command:  ## not an empty string: ''
            head = command[0:2]
            if head in filter_commands:
                continue
            if head in _unsupported_commands:
                continue
            command = inflate_hpgl_string_command(command)
            result.append(command)
    return result


@apply_logger
def inflate_hpgl_string_command(cmd_string):
    """Converts a string representing a single HPGL command into a
    Chiplotle HPGL instance.
    e.g., 'PD1,2,3,4' --> PD((1,2,3,4)).
    """
    head, body = _parse_hpgl_command_string(cmd_string)
    try:
        result = eval("hpgl.%s(%s)" % (head, body))
        return result
    except:
        msg = "Could not create %s(%s)..." % (head, body)
        msg += " The command is either malformed or unrecognized."
        inflate_hpgl_string_command.logger.warning(msg)


def _parse_hpgl_command_string(cmd_string):
    """Parses a single hpgl command string.
    Splits it in two: the head and the body.
    e.g., 'PD1,2,3,4' --> 'PD' and '(1,2,3,4)'.
    """
    head = cmd_string[0:2]
    if head in ("PU", "PD", "PA", "PR", "IP", "IW", "SC"):
        coords = cmd_string[2:].split(",")
        if coords == [""]:
            coords = []
        coords = [eval(n) for n in coords]
        coords = flat_list_to_pairs(coords)
        body = "(%s)" % coords
    elif head in ("RA", "RR", "ER", "EA"):
        body = "(%s)" % cmd_string[2:]
    elif head in ("AR", "AA"):
        parameters = cmd_string[2:].split(",")
        x = parameters.pop(0)
        y = parameters.pop(0)
        body = "(%s,%s),%s" % (x, y, ",".join(parameters))
    else:
        body = cmd_string[2:]
    return head, body


if __name__ == "__main__":
    string = "IN;PU;PD1,2,3,4;"
    print(inflate_hpgl_string(string))
