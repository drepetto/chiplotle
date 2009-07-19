********************
Quick Start Tutorial
********************


Chiplotle modes
===============

There are three main ways of using Chiplotle:

#. *Command line*: an interactive mode where you type in commands one at a time and the plotter executes them immediately.
#. *Python script*: you create an Python script that generates the desired Chiplotle commands and sends them to the plotter.
#. *HPGL pipeline*: you send pre-existing HPGL commands from a file to the plotter using Chiplotle as a simple serial interface.


Running Chiplotle from the command line
---------------------------------------

An easy way to get a feel for Chiplotle is to directly enter some commands 
via the command line.
Start Chiplotle by typing ``chiplotle`` from the terminal::

   $ chiplotle

.. note::
   If you've installed Chiplotle using Subversion, make sure the ``chiplotle/scritps`` directory is in your ``PATH`` variable so that your system knows about Chiplotle's scripts.

You'll see a listing of the serial ports available on your machine. 
Choose the one that you have your plotter plugged into.

Chiplotle will attempt to communicate with your plotter on that serial port, and if successful,
will print the ID string returned by the plotter. You will then be asked to select a plotter type.
Select the one that most closely matches the plotter ID. If there is no match, you can use the
generic Plotter, although you should be aware that some HPGL commands may not work with your plotter.

After you've selected a plotter type Chiplotle will print out some basic information about your 
plotter, including its drawing area. Now it's time to plot!

Let's pick up a pen. In HPGL, the command to pick up a pen is ``SP``, which stands for "select pen".
To learn what parameters you need to pass to a command, look it up in the "Chiplotle-HPGL" section
of the Chiplotle API documentation. Many commands take one or more parameters; if a command takes
parameters you put them inside a set of ``()`` after the command name. ``SP`` takes a pen number, and we 
want to select pen number one, so our command is ``SP(1)``. To pass the command to the plotter, you 
use ``plotter.write( )``. So::

   chiplotle> plotter.write(SP(1))

Your plotter should pick up pen one. Some common commands, like SP, have shortcuts in chiplotle. So
you can also do::

   chiplotle> plotter.selectPen(1)

to select pen number one. 

Now let's move the pen. To move the pen while it is in the up position, you use ``PU([x,y])``, and to move
the pen while it's down you use ``PD([x,y])``. x and y are the coordinates you want to move the pen to.
If you want to do a ``PU`` or ``PD`` without moving, just pass a blank set of coordinates.
So to draw a square you might do something like::

   chiplotle> plotter.selectPen(1)
   chiplotle> plotter.write(PU([100,100]))
   chiplotle> plotter.write(PD([200,100]))
   chiplotle> plotter.write(PD([200,200]))
   chiplotle> plotter.write(PD([100,200]))
   chiplotle> plotter.write(PD([100,100]))
   chiplotle> plotter.write(PU([]))

There are shortcuts for ``PU`` and ``PD``::

   chiplotle> plotter.penUp([100,100])
   chiplotle> plotter.penDown([100,100])

To replace the pen and have a look at your magnificent square, you select pen zero::

   chiplotle> plotter.selectPen(0)
   

You can also use Chiplotle's Compound commands, a set of more complex routines that we've
added to the basic HPGL command set::

    chiplotle> plotter.write(RandomWalk([500,500], 100))

That's it! Have a look at the Chiplotle API documentation for a complete list of 
HPGL commands and Chiplotle Compound commands.


Running chiplotle from a Python script
--------------------------------------

Simple drawings can be done by hand from the command line, but you'll quickly find that it's much
easier to put your commands into a Python script so that you can edit them, rerun them, etc. 
And of course since you're writing in Python, you can use all the features of the language in 
addition to the Chiplotle commands. 

It's very easy to create a Python script with Chiplotle commands. The first thing you usually need 
to do is import all of the HPGL commands from Chiplotle. So open a new text file and type::

   from chiplotle import *

Next you want your script to run the Chiplotle setup routine and import the plotter definition::

   plotter = instantiate_plotter( )

This lets you select the appropriate serial port and plotter ID, and imports 
the plotter object so that you can use the ``plotter.write( )`` method as 
in the command line examples above. Now you can simply enter a series of 
Chiplote commands::

   plotter.selectPen(1)
   plotter.write(PU([100,100]))
   plotter.write(PD([200,100]))
   plotter.write(PD([200,200]))
   plotter.write(PD([100,200]))
   plotter.write(PD([100,100]))
   plotter.selectPen(0)

and save your script as a .py file (see examples/square.py for an example). 
To use your new program just run it as you would any Python script::

   $ python square.py


A slightly more sophisticated Python script that draws a random zigzag::

   from chiplotle import *
   import random
   
   plotter = instantiate_plotter( )
   
   plotter.selectPen(1)
   
   for x in range(0, 1000, 10):
       y = random.randint(0, 1000)
       plotter.write(PD([x,y]))
       
   plotter.selectPen(0)


See the .py files in the examples and scripts folders for some more elaborate examples. 


HPGL pipeline
-------------

If you already have a file containing HPGL commands (from a CNC design package, old design data, etc), you can use Chiplotle to send those commands to your plotter. Your HPGL file will be a text file with commands like::

   SP1;
   PU100,100;
   PD200,100;
   PD200,200;
   PD100,100;
   PD100,100;
   SP0;


To plot the file while running Chiplotle you can use the plotter's own 
``writeFile(filename)`` method::

   chiplotle> plotter.writeFile('my_file.hpgl')  

You can also plot the file from the command line without first running 
Chiplotle by using the ``plothpgl`` script found in the scripts folder::

   $ plothpgl my_file.hpgl


Chiplotle will take care of all buffering and timing issues, so even large 
HPGL files should plot reliably. See ``examples/square.hpgl`` for a sample 
HPGL file.

