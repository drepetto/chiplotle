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

**Q:**
I installed chiplotle in Windowz 98. Unfortunately running ``chiplotle`` from the ``cmd`` shell does not work. Windowz  isn't recognizing the ``chiplotle`` command. 

**A:**
Windows is not very friendly with Chiplotle!
You will have to add Python (if not done so already) and the Chiplotle script files to your path. These are usually installed under ``C:\Python26`` and ``C:\Python26\Scripts``.

Windows has a built-in dialog for changing environment variables
(following guide applies to XP classical view): Right-click the icon for
your machine (usually located on your Desktop and called “My Computer”) and
choose Properties. Then, open the Advanced tab and click the
Environment Variables button.

     My Computer ‣ Properties ‣ Advanced ‣ Environment Variables

In this dialog, you can add or modify User and System variables. 

.. note:: 
   To change System variables, you need non-restricted access to your machine (i.e.  Administrator rights).

Another way of adding variables to your environment is using the set command::
     
     set PATH=%PATH%;C:\path\to\chiplotle_executable

To make this setting permanent, you could add the corresponding command
line to your ``autoexec.bat``. ``msconfig`` is a graphical interface to this file.

Viewing environment variables can also be done more straight-forward: The
command prompt will expand strings wrapped into percent signs automatically::

   echo %PATH%

.. note::
   Don't forget to also install ``hp2xx``.
