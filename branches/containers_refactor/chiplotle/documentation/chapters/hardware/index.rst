Hardware 
========

Serial cables
-------------

Not all serial cables will work with all (or any) pen plotters, so make sure you've got the right cable before you decide your plotter is broken!
Ideally you would want to get your plotter's operation manual to see the schematics of the serial cable it expects. Unfortunately these are sometimes hard to find. If you are completely in the dark, try `this cable <http://search.digikey.com/scripts/DkSearch/dksus.dll?Detail&name=AE1370-ND>`_. 
The schematics are `here <http://www.usa-assmann.com/specs/ak150-3-r.pdf>`_.
We have successfully used this cable with the Roland DX series.

.. note:: A 9 to 25 pin serial cable is usually what you need.



USB to Serial Adapters
----------------------

In Windowz, Chiplotle currently only supports **COM** ports to communicate with your plotter. On computers with real good-old RS-232 serial ports Chiplotle has no problem. Modern computers usually no longer have serial ports, so you need to use a USB to Serial interface to connect your plotter to your computer. Because Chiplotle only supports **COM** ports, what you need is a USB to Serial interface with drivers that supports VCP (Virtual COM Port), so that your USB to Serial interface shows up as a **COM** port. 
You may want to get USB to Serial interface with the `FTDI Chip <http://www.ftdichip.com>`_; it has VCP drivers and works well on Windowz. 



