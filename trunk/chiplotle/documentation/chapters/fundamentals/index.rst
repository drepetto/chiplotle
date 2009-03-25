**********************
Chiplotle fundamentals
**********************

Basic Chiplotle-HPGL commands
=============================

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


Moving commands
===============

Drawing commands
================

Plotting
========

