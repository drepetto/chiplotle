Chiplotle fundamentals
======================

Basic Chiplotle-HPGL commands
-----------------------------

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


All the standard HPGL commands are implemented in Chiplotle, and their class name corresponds to the two letter mnemonic used in the HPGL.


Compound Chiplotle commands
---------------------------

Chiplotle extends the basic HPGL command set by adding `compound` HPGL commands. These compound commands are higher level classes that draw more complex shapes by using the basic HPGL command set under the hood.

The `Circle` class, for example, generalizes the circle creation capabilities provided by HPGL. The `Circle` class has five attributes: `xy` position, `pen`, `radius`, `filled` and `chord`. To draw a filled circle at position `(10, 20)` with radius 1000 you would do::

   chiplotle> c = Circle((10, 20), 1000, filled = True, pen = 1)
   chiplotle> c.format
   'SP1;PU10.0,20.0;WG1000.0,0,359;'

Notice that to do this with pure HPGL you must effectively create the sequence of commands shown in the ``c.format`` output. In Chiplotle you would do::

   chiplotle> sp = SP(1)
   chiplotle> pu = PU((10, 20))
   chiplotle> wg = WG(1000, 0, 359)
   chiplotle> result = sp.format + pu.format + wg.format
   chiplotle> result
   'SP1;PU10.0,20.0;WG1000.0,0,359;'

This may seem like not much of a gain, but for more complex drawing structures, ecapsulating many HPGL subcommands in a single object can simplify things quit a bit. 


