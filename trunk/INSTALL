==========
Installing
==========


Dependencies 
============

To install Chiplotle you must already have Python 2.5 or Python 2.6 installed in your computer. 

Chiplotle has the following dependencies:

NumPy (for number crunching):
http://numpy.scipy.org/

PySerial (for serial communication):
http://pyserial.sourceforge.net/

hp2xx (for image export / hpgl preview):
http://www.gnu.org/software/hp2xx/hp2xx.html


Installing the official release
===============================

If you have the Python `setuptools <http://pypi.python.org/pypi/setuptools>`__ utility installed, simply type::

   easy_install -U chiplotle


If you don't have  *setuptools*, follow these steps:
 
1. Download the latest Chiplotle release from http://pypi.python.org/pypi/Chiplotle.

2. Untar the downloaded file (e.g. `tar xzvf Chiplotle-NNN.tar.gz`,
   where `NNN` is the version number of the latest release).

3. Change into the directory created in step 2 (e.g. `cd Chiplotle-NNN`).

4. If you're using Linux, Mac OS X or some other flavor of Unix, enter
   the command:: 
      
      sudo python setup.py install

   at the shell prompt.
   If you're using Windows, start up a command shell with administrator
   privileges and run the command ``setup.py install``.


These commands will install Chiplotle in your Python installation's `site-packages` directory. Note that this requires a working internet connection. 


Installing the development version
==================================

If you'd like to be at the cutting edge of the Chiplotle development use the following alternative:

1. Install Subversion if you don't have it already installed 
   (enter ``svn help`` to verify this).

2. Check out Chiplotle's `trunk` development like so::

      svn co svn://music.columbia.edu/chiplotle/trunk/ chiplotle-trunk

3. Make the Python interpreter aware of Chiplotle. 
   There are two ways to do this:

   a. Make a symlink in your Python `site-packages` directory pointing to 
   the chiplotle-trunk directory previously checked out via Subversion::
         
      ln -s 'pwd'/chiplotle-trunk/chiplotle SITE-PACKAGES-DIR/chiplotle

   where SITE-PACKAGES-DIR is the Python `site-packages` directory.
   In Linux this is usually in ``/usr/lib/Python2.x/site-packages``.

   b. Alternatively you can include the `chiplotle-trunk` directory in 
   your ``PYTHONPATH`` environment variable.             

4. Have your ``PATH`` environment variable point to the `scripts` folder. 
   This will allow you to run Chiplotle and all its accompanying scripts from 
   anywhere in your system.

5. Download and install NumPy and PySerial.

