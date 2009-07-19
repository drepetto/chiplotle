***
FAQ
***

**Q:** 
When I send a text file with HPGL commands to my serial port in the following way::

   $ stty /dev/ttyUSB0 9600
   $ cat bird.hpgl > /dev/ttyUSB0

my plotter starts drawing fine but will eventually just start pausing and drawing random straight lines. What's goind on? Do I have to be concerned with overflowing the plotter's internal RAM?

**A:**
Yes. The plotters buffer will fill up quickly, so you need to be listenning to the plotter for any buffer overflow warnings and errors. This is generally done in one of two ways:

#. Setting up hardware hand-shacking between the plotter and your computer. 
#. Querying the plotter for its buffer size before sending data to avoid truncation.

This is one of the tasks that Chiplotle manages for you so you don't have to worry about these low level technicalities.   
The easiest way to communicate with a plotter is to run Chiplotle by typing ``chiplotle`` from your terminal. 
This will prompt you for a serial port to choose from. Choose the serial port your plotter is connected to. Then choose the plotter type that most closely matches the one you have. If you are not sure, choose the generic 'Plotter'. This will create a ``plotter`` instance automatically for you. Once in Chiplotle (you will know by the ``chiplotle>`` prompt), send your HPGL file to the plotter via the ``write( )`` method, like so::

   chiplotle> f = open('bird.hpgl', 'r')
   chiplotle> my_file = f.read( )
   chiplotle> f.close( )
   chiplotle> plotter.write(my_file)  

The ``plotter`` does the buffer managing for you.

If you don't want to work 'on line' and want to run your Python scripts,
instead of running the executable ``chiplotle`` you can instantiate your own plotter in your scripts with the correct serial port. e.g. ::

   from chiplotle import *
   from serial import *
   s = Serial('/dev/ttyUSB0')
   p = Plotter(s)

then send hpgl commands::

   p.write(PA( ))


------

**Q:**
Is there a facility in Chiplotle to send over already existing HPGL command files? 

**A:**
Yes. Chiplotle comes with the ``plothpgl`` executable script designed exactly for this purpose. To send HPGL files to your plotter simply run the script from the command prompt with the file as the argument::

   $ plothpgl my_file.hpgl

To see the usage instructions run ``plothpgl`` with no arguments. Note that Chiplotle simply pipes the file to the plotter and does not check the syntax of the HPGL file.

You can also send HPGL files to your plotter from within a live Chiplotle session using a Plotter's own ``writeFile(filename)`` method, like so::

   chiplotle> plotter.writeFile('my_file.hpgl')  
