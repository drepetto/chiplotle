from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
import os

__version__ = '0.4.1'

home_path = os.environ.get('HOME') or os.environ.get('HOMEPATH')

CHIPLOTLE_DIR = os.path.dirname(__file__).rstrip('cfg')
CONFIG_DIR = os.sep.join([home_path, '.chiplotle'])
CONFIG_FILE = os.sep.join([home_path, '.chiplotle', 'config.py'])
LOG_FILE = os.sep.join([home_path, '.chiplotle', 'session.log'])
