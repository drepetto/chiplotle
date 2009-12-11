from serial import Serial
import sys
import time

def is_plotter_alive(ser, wait_time=5):
      '''Check if there's a powered-on plotter in *ser* port.
      
      - *ser* : a Serial object.
      - *wait_time* : ``int`` maximum time in seconds to wait for 
         plotter response.'''
      
      assert isinstance(wait_time, int)
      assert isinstance(ser, Serial)

      print 'Waiting for reply from plotter...',

      ser.flushInput()
      ser.flushOutput()
      ser.write('IN;')
      ser.write('OI;')

      for i in range(1, wait_time + 1):
         if ser.inWaiting( ) > 0:
            print "got reply from plotter.\n"
            return True
         else:
            time.sleep(1)

      print 'ERROR: no plotter found in port %s or plotter not on.' % ser.port
      return False
