from serial import Serial
import sys
import time

def is_plotter_alive(serial, wait_time=5):
      '''Check if there's a powered-on plotter in *serial* port.
      
      - *serial* : a Serial object.
      - *wait_time* : ``int`` maximum time in seconds to wait for 
         plotter response.'''
      
      assert isinstance(wait_time, int)
      assert isinstance(serial, Serial)

      serial.flushInput()
      serial.flushOutput()

      serial.write('IN;')
      serial.write('OI;')
      
      print 'Waiting for reply from plotter...'

      for i in range(1, wait_time + 1):
         if serial.inWaiting( ) > 0:
            print "Got reply to 'OI' from plotter.\n"
            return True
         else:
            time.sleep(1)
      else:
         return False
