import os

home_path = os.environ.get('HOME') or os.environ.get('HOMEPATH')

CHIPLOTLE_DIR = os.path.dirname(__file__).rstrip('cfg')
CONFIG_DIR = os.sep.join([home_path, '.chiplotle'])
CONFIG_FILE = os.sep.join([home_path, '.chiplotle', 'config.py'])
#CONFIG_FILE = os.sep.join([home_path, '.chiplotle', 'config'])
