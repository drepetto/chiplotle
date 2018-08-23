Configuration
==============

Chiplotle has a dedicated folder, ``$HOME/.chiplotle``, which houses the ``config.py`` configuration file. This file is used to set a variety of configuration and preference values. The file is executed as a Python module, so its syntax must conform with standard Python syntax. Edit this file to change your Chiplotle default settings.

At present, the ``config.py`` file allows for the setting of the following parameters: 

* *Serial port to plotter map*: This is a dictionary that maps hardware devices (e.g. 'dev/ttyS0') to software Chiplotle plotters (e.g., 'DXY-1300').  Set it to `None` if you want Chiplotle to dynamically find the plotters connected to your computer. This is the default, and can be convenient when your setup changes frequently. For a fixed setup set this to a dictionary mapping serial ports to plotters. 

* *Serial connection parameters*: These are the serial communication parameters that *all* your connected plotters must be set to. Chiplotle sets these to common standard values. Make sure your hardware plotter is set to these values, or change them to match those of your hardware.

* *Maximum plotter "wait for response" time*: Plotters take some time to respond to your queries. Set this to the maximum time you expect your plotter to wait for a response.

* *Verbosity*: Chiplotle keeps a log of important events taking place during a Chiplotle session in the ``session.log`` file under your ``.chiplotle`` directory. Set verbosity to ``True`` if you want all the log information to be displayed in the screen during execution.
