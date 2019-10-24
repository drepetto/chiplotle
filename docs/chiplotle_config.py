## Chiplotle configuration file.
## Created by Chiplotle on 21 August 2018 20:52:20.
##
## This file houses all the configuration variables employed
## by Chiplotle. You can set them manually to suit your needs.
## Do not delete them! If you want them to have no effect
## simply set them to "None".
##
## This file is executed via the ``execfile( )`` function,
## so all its content should adhere to the Python syntax.


# Configuration Variables ---------------------------------

## Serial ports to plotters map.
## Set to None if you want Chiplotle to dynamically find the
## plotters connected to your computer. This is the default.
## This default is convenient when your setup changes frequently.
## For a fixed setup set this to a dictionary mapping serial
## ports to plotters.
## e.g., {'/dev/ttyS0' : 'DXY-1300', '/dev/ttyS1' : 'HP7475A'}
## sets plotter 'DXY-1300' to port '/dev/ttyS0' and plotter
## 'HP7475A' to port '/dev/ttyS1'.
serial_port_to_plotter_map = {'/dev/usb/lp0': 'DXY-1300'}


## Serial connection parameters.
## Set your plotter to match these values, or vice versa..
baudrate = 9600
bytesize = 8
parity = 'N'
stopbits = 1
timeout = 1
xonxoff = 1
rtscts = 0


## Maximum wait time for response from plotter.
## Every time the plotter is queried, Chiplotle will wait for
## a maximum of `maximum_response_wait_time` seconds.
maximum_response_wait_time = 8


## Set to True if you want information (such as warnings)
## displayed on the console. Set to False if you don't.
verbose = True


