#!/usr/bin/env python
from chiplotle import *

def envelope( ):
   plotter = instantiate_plotters( )[0]

   to_address = []
   from_address = []

   print ("\n\renter FROM ADDRESS (blank line to end):")

   finished = 0
   while finished == 0:
    
      line = raw_input("")
      if len(line) == 0:
         finished = 1
      else:
         from_address.append(line)

   print ("enter TO ADDRESS (blank line to end):")

   finished = 0
   while finished == 0:

      line = raw_input("")
      if len(line) == 0:
         finished = 1
      else:
         to_address.append(line)

   input = raw_input("\n\renter pen number for plotting FROM ADDRESS:\n")
   pen_num = int(input)

   plotter.write(SP(pen_num))

   raw_input("\n\rmove pen to top left of FROM: address field and hit return to start plotting...")
   print("plotting FROM: address...")

   for line in from_address:
      plotter.write(LB(line))
      plotter.write(LB("\n\r"))

   input = raw_input("\n\renter pen number for plotting TO ADDRESS:\n")
   pen_num = int(input)

   plotter.write(SP(pen_num))

   raw_input("\n\rmove pen to top left of TO ADDRESS field and hit return to start plotting...")
   print("plotting TO ADDRESS...")

   num_lines = len(to_address)
   line_num = 0

   for line in to_address:
      plotter.write(LB(line))
      plotter.write(LB("\n\r"))

   plotter.write(SP(0))
   print("done!")


if __name__ == '__main__':
   envelope( )
