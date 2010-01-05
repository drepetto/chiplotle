Configuration
==============

Chiplotle has a dedicated folder, ``$HOME/.chiplotle``, which houses the 
``config.py`` configuration file. This file is for setting various
preferences and defaults. The file is executed as a Python module, so its syntax must conform with standard Python syntax. 

At present a default *serial port* is supported.

To set your default serial port, set the ``serial_port =`` line in the 
``config.py`` file to the path of your serial port, in string format.

.. note:: 
   In POSIX type operating systems these ports are under the /dev directory. Serial ports usually look like ttyS0, ttyS1, etc. If you have a computer with no serial port and you are using a serial to USB converter then these ports might look like ttyUSB0, ttyUSB1, etc. 


If this variable is not set, Chiplotle will interactively ask you what port and plotter you want to use when you run it in  *command line* mode via the ``chiplotle`` terminal script.  

