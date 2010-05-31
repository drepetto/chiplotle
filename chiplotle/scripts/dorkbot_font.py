#!/usr/bin/env python

from chiplotle import *
from chiplotle.hpgl.compound.dorkbotlabel import DorkbotLabel


def main():
   
   print("****************")
   print("* DORKBOT FONT *")
   print("****************")
   
   plotter = instantiate_plotters( )[0]

   input = raw_input("enter font outline pen number:")
   outline_pen = int(input)

   fill_pen = None
   input = raw_input("enter font fill pen number (hit Enter for no outline):")
   if input:
      fill_pen = int(input)

   input = raw_input("enter font outline jitter:")
   outline_jitter = [int(input)] * 2

   fill_jitter = None
   if fill_pen:
      input = raw_input("enter font fill jitter:")
      fill_jitter = [int(input)] * 2 

   input = raw_input("enter font style (1 = square, 2 = circles):")
   styles = {'1':'square', '2':'circle'}
   font_style = styles[input]
   
   input = raw_input("enter font width in plotter points:")
   width = int(input)
   
   while True:   
      text = raw_input("enter text to plot (blank line to end):")
      if not text:
         break

      msg = "move to top left corner and hit enter to begin plotting..."
      raw_input(msg)
      
      point_string = plotter.actual_position
      point_string_parts = point_string.split(',')
      x = int(point_string_parts[0])
      # the "- cell_size is there because rects are drawn from the 
      # bottom left
      # corner, but we've put our starting point at the top left
      y = int(point_string_parts[1])  
   
      text = DorkbotLabel((x, y), text, font_style, outline_pen, fill_pen,
        width, outline_jitter = outline_jitter, fill_jitter = fill_jitter)
      plotter.write(text)
   
   plotter.pen_up()

if __name__ == '__main__': main()

