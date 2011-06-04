Chiplotle fundamentals
======================

*Chiplotle* is a Python library for procedural / algorithmic drawing specifically designed to control pen plotters. While other drawing computer tools are designed to create art on the screen (or for ordinary printing), Chiplotle knows about and understands the mechanics of drawing with pen plotters, or cutting with machine cutters. 

How does Chiplote communicate with these wonderful machines?
During the 70s and 80s, a variety of languages were developed by different manufacturers to control different brands of pen plotters, but the one language that gained most popularity and eventually became sort of a standard is HPGL (Hewlett-Packard Graphics Language). 
Chiplotle supports all the standard HPGL commands, giving the user full control of these plotters. 

With Chiplotle the user has direct access both the the HPGL commands and to higher abstract shapes that generate the necessary HPGL code to generate these shapes. Thus, one can think of Chiplotle as consisting of three layers:

#. A high abstraction layer consisting of platonic shapes, like `line`, `circle`, `label`, etc.'
#. An interface / communication layer consisting of the HPGL language.
#. A hardware layer consisting of the plotting machine itself.

Further, Chiplotle provides plotter interfaces that allow the user to contol the plotter as if through a control panel. 


Chiplotle geometry
*****************************

Shapes
------

Chiplotle comes built in with a set of common shapes, like `line`, `circle`, `rectangle`, `ellipse`, etc.


Transforms
-----------

Core classes
------------



Chiplotle-HPGL commands
*****************************

Each HPGL command in Chiplotle is implemented as a Class. Chiplotle HPGL commands can be instantiated as you would normally instantiate any other class. Some commands require arguments, others don't::

   chiplotle> PD( )
   PD(xy=[])

   chiplotle> CI(10)
   CI(chordangle=None, radius=10.0)

All Chiplotle HPGL commands have a ``format`` attribute. This attribute returns a string representation of the HPGL command as sent to the plotter.
::

   chiplotle> t = PD( )
   chiplotle> t.format
   'PD;'


All the standard HPGL commands are implemented in Chiplotle, and their class names corresponds to the two letter mnemonic used in the HPGL.
Refer to the :doc:`Chiplotle API </chapters/api/chiplotle_hpgl>` for a list and documentation of all the HPGL commands.

