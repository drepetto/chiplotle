from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import open
from future import standard_library

standard_library.install_aliases()
from chiplotle.core.cfg.cfg import CONFIG_FILE


def read_config_file():
    """Read the content of the config file ``$HOME/.chiplotle/config.py``.
    Returns a dictionary of ``var : value`` entries."""

    globals = {}
    locals = {}
    exec(compile(open(CONFIG_FILE).read(), CONFIG_FILE, "exec"), globals, locals)
    return locals
