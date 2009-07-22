Configuration
==============


Chiplotle has a dedicated folder, ``$HOME/.chiplotle``, which houses the 
``config`` configuration file. This file is for setting various
preferences and defaults. At present a default *serial port* and a preferred 
*plotter type* are supported.

To set your default serial port, set the ``serial_port=`` line in the 
``config`` file.

.. note:: 
   In POSIX type operating systems these ports are under the /dev directory. Serial ports usually look like ttyS0, ttyS1, etc. If you have a computer with no serial port and you are using a serial to USB converter then these ports might look like ttyUSB0, ttyUSB1, etc. 

To set your default plotter, set the ``plotter_type=`` to a valid plotter type. 

If these variables are not set, Chiplotle will interactively ask you what port and plotter to use when run it in  *command line* mode via the ``chiplotle`` terminal script.  

