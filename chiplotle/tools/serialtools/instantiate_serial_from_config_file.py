from chiplotle.cfg.read_config_file import read_config_file
import serial

def instantiate_serial_from_config_file(port):
   '''Instantiates a Serial with port `port` and serial config
   parameters read from the configuration file.'''
   config = read_config_file( )
   ser = serial.Serial(port = port, 
      bytesize = config['bytesize'], 
      parity = config['parity'], 
      stopbits = config['stopbits'], 
      timeout = config['timeout'],
      xonxoff = config['xonxoff'],
      rtscts = config['rtscts'])
   return ser
