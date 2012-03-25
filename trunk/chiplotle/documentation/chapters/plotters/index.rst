Plotters
========


Plotter Device Files
---------------------------------------

Chiplotle comes with device files for a number of plotters from different manufactuers,
including Hewlett-Packard and Roland. Look in the /chiplotle/plotters folder to see if 
there's a device file that matches your plotter. If not, then look in your plotter manual
to see if it emulates any of those plotters. For example, plotters by other 
manufacturers often emulate the HP7475a. 

See :doc:`Configuration </chapters/configuration/index>` for info on telling Chiplotle which device file you'd like to use. 

.. note:: If Chiplotle does not have a device file for your plotter and you'd like to help us create one, all you need to do is send us the list of commands that your plotter recognizes and the ID string that it presents when Chiplotle opens it. 


Offline Plotting
---------------------------------------

Sometimes you may want to work on your plotter code without having to actually connect your plotter and physically plot every command. There are several ways to use Chiplotle offline:


* Run python (not the chiplotle script!) and collect your commands into a Group, tuple or string, and when you want to see the results send the collected commands to ``io.view( )``. This method works well when you're generating commands algorithmically and don't need any interaction with the plotter::

   >>> from chiplotle import *
   >>> commands = []
   >>> commands.append(SP(1))
   >>> commands.append(PA([(0,0)]))
   >>> commands.append(PD())
   >>> commands.append(PA([(1000,1000)]))
   >>> commands.append(PU())
   >>> commands.append(SP(0))
   >>> io.view(commands)
   
* The above technique can also be used to write your commands out to an hpgl file for later viewing with your favorite hpgl viewer/converter::

   >>> io.save_hpgl(commands, "diagonal.plt")
   
* Use a virtual serial port. This method allows you to simulate "live plotting," including sending queries to the plotter (for example, to find out where the pen is) or responding to user input.::

   >>> from chiplotle import *
   >>> from chiplotle.tools.plottertools import instantiate_virtual_plotter
   >>> plotter =  instantiate_virtual_plotter(type="HP7550A")
   >>> plotter.margins.hard.draw_outline()
   >>> plotter.select_pen(2)
   >>> plotter.goto(0,0)
   >>> plotter.pen_down()
   >>> plotter.goto(1000,1000)
   >>> plotter.pen_up()
   >>> plotter.select_pen(0)
   >>> io.view(plotter)
   
.. note:: ``io.view()`` requires `hp2xx <http://www.gnu.org/software/hp2xx>`_ to be installed on your system in order to convert the hpgl files into postscript for viewing by your OS's native ps viewer application.
