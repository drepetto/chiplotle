# right now it just prints out the font with a letter you select
# we need to capture the starting location so that we can go back there 
# for subsequent letters

import random, math

from chiplotle import *
from chiplotle.utils.run_chiplotle_UNIX import plotter
from chiplotle.examples import dorkbot_font_defs as font

random.seed()

print("****************")
print("* DORKBOT FONT *")
print("****************")

input = raw_input("enter font outline pen number:")
outline_pen = int(input)
input = raw_input("enter font fill pen number:")
fill_pen = int(input)
input = raw_input("enter font outline jitter (0-100):")
outline_jitter = int(input) / 100.0
input = raw_input("enter font fill jitter (0-100):")
fill_jitter = int(input) / 100.0
input = raw_input("enter font style (0 = rects, 1 = circles, 2 = Xs):")
font_style = int(input)

if font_style == 2:
	x_char = raw_input("enter character to use for Xs:")

input = raw_input("enter font cell size in plotter points:")
cell_size = int(input)

text = raw_input("enter text to plot:")

plotter.write(SP(outline_pen))

input = raw_input("move to top left corner and hit enter to begin plotting...")
print("plotting...")

point_string = plotter.actualPosition
point_string_parts = point_string.split(',')
origin_x = int(point_string_parts[0])
start_x = origin_x
# the "- cell_size is there because rects are drawn from the bottom left
# corner, but we've put our starting point at the top left
origin_y = int(point_string_parts[1]) - cell_size
start_y = origin_y

print("starting point x: " + str(start_x) + " y: " + str(start_y))

# first do all outlines
for cur_char in text:
	print("plotting character outline: " + cur_char)
	character = font.char_dict[cur_char]

	cell_col = 0
	cell_row = 0
	
	while cell_row < 7:
	
		seg_num = cell_col + (cell_row * 3)

		if character[seg_num] == 1:
			jiggle_outline_x = math.floor(random.random() * outline_jitter * cell_size) - (0.5 * outline_jitter * cell_size)
			jiggle_outline_y = math.floor(random.random() * outline_jitter * cell_size) - (0.5 * outline_jitter * cell_size)

			x_outline = start_x + (cell_col * cell_size) + jiggle_outline_x
			y_outline = start_y - (cell_row * cell_size) + jiggle_outline_y
			
			if font_style == 0:				
				plotter.goto(x_outline, y_outline)
				plotter.write(ER([cell_size,cell_size]))
			elif font_style == 1:
				plotter.goto(x_outline + cell_size/2, y_outline + cell_size/2)
				plotter.write(CI(cell_size/2))
	
		cell_col = cell_col + 1
		if cell_col == 3:
			cell_col = 0
			cell_row = cell_row + 1

	start_x = start_x + (cell_size * 3) + (cell_size/2)



# now do all fills

plotter.write(SP(fill_pen))

start_x = origin_x
start_y = origin_y

for cur_char in text:
	print("plotting character fill: " + cur_char)
	character = font.char_dict[cur_char]	
	cell_col = 0
	cell_row = 0

	while cell_row < 7:
	
		seg_num = cell_col + (cell_row * 3)

		if character[seg_num] == 1:
			jiggle_fill_x = math.floor(random.random() * fill_jitter * cell_size) - (0.5 * fill_jitter * cell_size)
			jiggle_fill_y = math.floor(random.random() * fill_jitter * cell_size) - (0.5 * fill_jitter * cell_size)

			x_fill = start_x + (cell_col * cell_size) + jiggle_fill_x
			y_fill = start_y - (cell_row * cell_size) + jiggle_fill_y
			
			if font_style == 0:
				plotter.goto(x_fill, y_fill)
				plotter.write(RR([cell_size,cell_size]))
			elif font_style == 1:
				plotter.goto(x_fill + cell_size/2, y_fill + cell_size/2)
				plotter.write(WG(cell_size/2, 0, 360))
	
		cell_col = cell_col + 1
		if cell_col == 3:
			cell_col = 0
			cell_row = cell_row + 1

	start_x = start_x + (cell_size * 3) + (cell_size/2)
		
plotter.write(SP(0))

	
#	while seg_num < 21:
#		if character[seg_num] == 1:
#			if font_style == 2:
#				plotter.write(LB(x_char))
#		else:
#			if font_style == 2:
#				plotter.write(LB(" "))
#		
#		seg_num += 1
#		
#		if seg_num % 3 == 0:
#			if font_style == 2:
#				plotter.write(LB("\n\r"))
		



		
