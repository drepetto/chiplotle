***
FAQ
***

**Q:**
I'm trying to use Chiplotle with Windowz but it seems Chiplotle can't find my hardware. What should I do?

**A:**
No communication between Chiplotle and your hardware could be due to a variety of reasons. Check out the :doc:`Hardware </chapters/hardware/index>` section for some possible causes.


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
This will run python and load, Chiplotle library, and instantiate soft-plotters for your hardware plotters found. Once in Chiplotle, send your HPGL file with the ``write_file(filename)`` method of the instantiated plotter(s), or send newly createdHPGL commands via the ``write( )`` method, like so::

   chiplotle> plotter.write_file('my_file.hpgl')  
   chiplotle> plotter.write(PA( ))


The ``plotter`` does the buffer managing for you.
See the :doc:`Tutorial </chapters/tutorial/index>` for more details.


**Q:**
Is there a facility in Chiplotle to send over already existing HPGL command files? 

**A:**
Yes. Chiplotle comes with the ``plot_hpgl_file.py`` executable script designed exactly for this purpose. To send HPGL files to your plotter simply run the script from the command prompt with the file as the argument::

   $ plot_hpgl_file.py my_file.hpgl

To see the usage instructions run ``plot_hpgl_file.py`` with no arguments. Note that Chiplotle simply pipes the file to the plotter and does not check the syntax of the HPGL file.

You can also send HPGL files to your plotter from within a live Chiplotle session using a Plotter's own ``write_file(filename)`` method, like so::

   chiplotle> plotter.write_file('my_file.hpgl')  
