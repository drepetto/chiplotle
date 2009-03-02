import os

home_path = os.environ.get('HOME') or os.environ.get('HOMEPATH')

CHIPLOTLE_DIR = os.path.dirname(__file__).rstrip('cfg')
CHIPLOTLE_SETTINGS = os.sep.join([home_path, '.chiplotle', 'settings.cfg'])
