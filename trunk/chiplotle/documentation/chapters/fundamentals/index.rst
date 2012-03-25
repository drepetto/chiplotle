Chiplotle fundamentals
======================

.. warning:: This section needs fleshing out.

In addition to being an HPGL plotter driver, *Chiplotle* is a vector drawing librarly specifically designed to work with these HPGL plotters. While other drawing computer tools are designed to create art on the screen (or for ordinary raster printing), Chiplotle knows about and understands some of the mechanics of drawing with pen plotters. 

One can think of Chiplotle as consisting of three layers:

#. A high abstraction layer consisting of platonic shapes, like `line`, `circle`, `label`, etc.'
#. An interface / communication layer consisting of the HPGL language.
#. A plotter driver wich manages communication between your hardware and software.

HPGL
****

How does Chiplote communicate with a plotter?
During the 70s and 80s, a variety of languages were developed by different manufacturers to control different brands of pen plotters, but the one language that gained most popularity and eventually became sort of a standard is HPGL (Hewlett-Packard Graphics Language). 

Chiplotle supports all the standard HPGL commands, giving you full control of these plotters. 

Further, Chiplotle provides plotter interfaces that allow you to contol the plotter as if through a control panel. 


Chiplotle vector drawing
************************

In addition to being an HPGL plotter driver, Chiplotle is also a general purpose vector drawing librarly. 
With Chiplotle you can create generic shapes that can be sent to an HPGL plotter directly for drawing, without you knowing anything about the underlying HPGL language. 



Chiplotle geometry
*****************************

Shapes
------

Chiplotle comes built in with a set of common shapes, like `line`, `circle`, `rectangle`, `ellipse`, etc.

These shapes are agnostic of any particular drawing language, such as HPGL or g-code. 


Transforms
-----------

Chiplotle allows you to apply your standard geometric transformations to any shapes you may create with it. 



Chiplotle-HPGL commands
*****************************

In addition to the generic shape constructors, in Chiplotle you have access to specific HPGL command definitions. 

All the standard HPGL commands are implemented in Chiplotle, and their class names corresponds to the two letter mnemonic used in the HPGL.
Refer to the :doc:`Chiplotle API </chapters/api/hpgl>` for a list and documentation of all the HPGL commands.

Chiplotle HPGL commands can be instantiated as you would normally instantiate any other class. Some commands require arguments, others don't::

   chiplotle> PD( )
   PD(xy=[])

   chiplotle> CI(10)
   CI(chordangle=None, radius=10.0)

All Chiplotle HPGL commands have a ``format`` attribute. This attribute returns a string representation of the HPGL command as sent to the plotter.
::

   chiplotle> t = PD( )
   chiplotle> t.format
   'PD;'

