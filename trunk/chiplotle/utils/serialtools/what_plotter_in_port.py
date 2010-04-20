from chiplotle.cfg.read_config_file import read_config_file
import serial
import time

def what_plotter_in_port(port, wait_time=10):
   '''Check if there's a powered-on plotter in `port` port.
   
   - `port` : a string with port path or name.
   - `wait_time` : ``int`` maximum time in seconds to wait for 
      plotter response.

   Returns the ID of the plotter found or None.'''
   
   assert isinstance(wait_time, int)
   if not isinstance(port, basestring):
      raise TypeError('`port` must be a string.')

   from chiplotle.utils.serialtools import instantiate_serial_from_config_file
   ser = instantiate_serial_from_config_file(port)
   try:
      ser.flushInput()
      ser.flushOutput()
      ser.write('OI;')
   except serial.serialutil.SerialException:
      return None

   t = time.time( )
   while time.time( ) - t < wait_time:
      if ser.inWaiting( ) > 0:
         id = ser.readline(eol='\r').strip('\r')
         return id
