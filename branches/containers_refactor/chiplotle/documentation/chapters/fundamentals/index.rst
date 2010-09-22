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
Refer to the :doc:`Chiplotle API </chapters/api/chiplotle_hpgl>` for a list and documentation of all the HPGL commands.


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

These generalized basic geometric shapes also allow one to draw shapes that are simple, yet unavailable in the standard HPGL command set. The :class:`Rectangle <chiplotle.hpgl.compound.rectangle.Rectangle>` class, for example, allows us to draw rotated rectangles::  
   
   chiplotle> 
   chiplotle> r = Rectangle((1000, 2000), 250, 2000, 3.1416 / 4.) 
   chiplotle> r.format
   'PU;PA1618.72,2795.49;PD;PA1795.5,2618.72;PA381.28,1204.51;PA204.504,1381.28;PA1618.72,2795.49;PU;'


This may seem like not much of a gain, but for more complex drawing structures, encapsulating many HPGL subcommands in a single object can simplify things quit a bit. 
For example, the :class:`MayaNumber <chiplotle.hpgl.compound.mayanumber.MayaNumber>` class is a compound Chiplotle command that makes the creation of Maya numbers trivial by creating higher level geometric objects out of basic Chiplotle-HPGL commands::   

   chiplotle> mn = MayaNumber((1000, 2000), 563, size = 500)
   chiplotle> mn.format
   'PA1250.0,3187.5;CI35.7142868042;PU;PA1062.5,2589.29;EA1437.5,2660.71;PA1125.0,2750.0;CI35.7142868042;PA1250.0,2750.0;CI35.7142868042;PA1375.0,2750.0;CI35.7142868042;PA1125.0,2062.5;CI35.7142868042;PA1250.0,2062.5;CI35.7142868042;PA1375.0,2062.5;CI35.7142868042;'

PUT PICTURE HERE

Compound Chiplotle commands have another special property that plain Chiplotle-HPGL commands don't have. Compound commands can be hierarchically grouped via the :class:`Container <chiplotle.hpgl.compound.container.Container>` class.  

This class can hold other Compound classes to later be treated as a single object:: 

   chiplotle> c = Circle((1000, 2000), 1000)
   chiplotle> r = Rectangle((1000, 2000), 250, 2000, 3.1416 / 4.)
   chiplotle> cnt = Container((5000, 0), [c, r])
   chiplotle> cnt.format
   'PU6000.0,2000.0;CI1000.0;PU;PA6618.72,2795.49;PD;PA6795.5,2618.72;
   PA5381.28,1204.51;PA5204.5,1381.28;PA6618.72,2795.49;PU;'

Notice that, like all Chiplotle Compound commands, the :class:`Container <chiplotle.hpgl.compound.container.Container>` class also has an `xy` property::

   chiplotle> cnt.xy
   [ 5000.  0.]

Unlike the standard Chiplotle-HPGL commands, these  compound commands also have **absolute** positional properties. The settable `xy` positional property defines the position of the object relative to the container it lives in, if any. The absolute `xyabsolute` property defines the object's absolute location in the page. These absolute position attributes are not settable. So, in the example above, because the circle and the rectangle are contained in the `cnt` :class:`Container <chiplotle.hpgl.compound.container.Container>`  object, they will move with the container whenever we change it's position::

   chiplotle> cnt.xy = (-2000, -10000)
   chiplotle> c.xy
   [ 1000.  2000.]
   chiplotle> c.xyabsolute
   [-1000. -8000.]
   chiplotle> r.xyabsolute
   [-1000. -8000.]
   chiplotle> c.xy
   [ 1000.  2000.]
   chiplotle> r.xy
   [ 1000.  2000.]
   chiplotle> cnt.format
   'PU-1000.0,-8000.0;CI1000.0;PU;PA-381.28,-7204.51;PD;PA-204.504,-7381.28;
   PA-1618.72,-8795.49;PA-1795.5,-8618.72;PA-381.28,-7204.51;PU;


Refer to the :doc:`Chiplotle API </chapters/api/chiplotle_compound>` for a list of the compound Chiplolte commands currently available.
   


Chiplotle transform functions
-----------------------------

All Chiplotle drawing classes --both the base Chiplotle-HPGL and the compound commands-- can be scaled and displaced with the ``scale( )`` and ``transpose( )`` functions found in the ``hpgltools`` module, provided their properties are **scalable** and **transposable**, respectively::

   chiplotle> c = Circle((1000, 2000), 1000)
   chiplotle> c.xy
   [ 1000.  2000.]
   chiplotle> c.radius
   1000.0
   chiplotle> hpgltools.scale(c, 2)
   chiplotle> c.xy
   [ 2000.  4000.]
   chiplotle> c.radius
   2000.0

::

   chiplotle> hpgltools.transpose(c, (-1000, -500))
   chiplotle> c.xy
   [ 1000.  3500.]
   chiplotle> c.radius
   2000.0

Notice how, while both the `xy` position and the `radius` properties are scalable in the :class:`Circle <chiplotle.hpgl.compound.circle.Circle>`  class, only `xy` is transposable. This makes sense, you don't want your radius to change when you move the circle!

