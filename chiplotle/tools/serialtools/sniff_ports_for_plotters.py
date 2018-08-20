from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from future import standard_library
standard_library.install_aliases()
def sniff_ports_for_plotters(ports):
    '''Sniffs all given serial `ports` in search for pen plotters.
    The function returns a dictionary of plotter names found, with keys
    being the port name or address and values the plotter names.'''
    from chiplotle.tools.serialtools import what_plotter_in_port

    plotters_found = { }
    #for k, port in scan_serial_ports( ).items( ):
    for port in ports:
        plotter_name = what_plotter_in_port(port)
        if plotter_name:
            plotters_found[port] = plotter_name

    return plotters_found
