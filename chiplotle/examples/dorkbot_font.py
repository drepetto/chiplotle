# right now it just prints out the font with a letter you select
# we need to capture the starting location so that we can go back there 
# for subsequent letters


from chiplotle import *
from chiplotle.utils.run_chiplotle_UNIX import plotter
from chiplotle.examples import dorkbot_font_defs as font

print("****************")
print("* DORKBOT FONT *")
print("****************")

input = raw_input("enter font outline pen number:")
outline_num = int(input)
input = raw_input("enter font fill pen number:")
fill_num = int(input)
input = raw_input("enter font outline jitter (0-10):")
outline_jitter = int(input)
input = raw_input("enter font fill jitter (0-10):")
fill_jitter = int(input)
input = raw_input("enter font style (0 = rects, 1 = circles, 2 = Xs):")
font_style = int(input)

if font_style == 2:
	x_char = raw_input("enter character to use for Xs:")

input = raw_input("enter font size (1-5):")
font_size = int(input)

text = raw_input("enter text to print:")

input = raw_input("move to top left corner and hit enter to begin plotting...")
print("plotting...")

plotter.write(SP(outline_num))

for cur_char in text:
	print ("got char: ")
	print cur_char
	print ("looking it up...")
	character = font.lookup_char(cur_char)
	print character
	
	seg_num = 0
	
	while seg_num < 21:
		if character[seg_num] == 1:
			if font_style == 2:
				plotter.write(LB(x_char))
		else:
			if font_style == 2:
				plotter.write(LB(" "))
		
		seg_num += 1
		
		if seg_num % 3 == 0:
			if font_style == 2:
				plotter.write(LB("\n\r"))
		



		