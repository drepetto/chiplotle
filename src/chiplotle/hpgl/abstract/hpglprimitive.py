from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import str
from future import standard_library

standard_library.install_aliases()
from chiplotle.hpgl.abstract.hpgl import _HPGL


class _HPGLPrimitive(_HPGL):

    _terminator = b";"

    @property
    def format(self):
        return b"%s%s" % (self._name, _HPGLPrimitive._terminator)

    ### OVERRIDES ###

    ### TODO: [VA] make this simpler. remove all but the name?
    def __repr__(self):
        attributes = []
        for attribute in sorted(dir(self)):
            if not attribute.startswith("_"):
                if not callable(getattr(self, attribute)):
                    # if a not in ('x', 'y', 'format', 'terminator'):
                    if attribute not in ("x", "y", "format"):
                        attributes.append("%s=%s" % (attribute, str(getattr(self, attribute))))
        result = "%s(%s)" % (self._name.decode('ascii'), ", ".join(attributes))
        return result
