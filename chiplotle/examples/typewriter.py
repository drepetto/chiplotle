from chiplotle import *
from chiplotle.utils.run_chiplotle_UNIX import plotter


print("***************************")
print("* CHIPLOTLE TYPEWRITER!!! *")
print("***************************")
print("")

pen_num = int(raw_input("which pen? "))

set_size = raw_input("set font size (y/N)? ")

if set_size == "y":
	char_height = float(raw_input("font height (in cm)? "))
	char_width = float(raw_input("font width (in cm)? "))
	plotter.write(SI(char_width, char_height))

plotter.selectPen(pen_num)

print("")
print("type at the >>> prompt.")
print("press RETURN after each line to be plotted.")
print("enter a blank line for options.")
print("")

finished = False

while finished == False:
	line = raw_input(">>>")
	if len(line) == 0:
		print("(enter): blank line")
		print("p: select new pen")
		print("s: set new font size")
		print("q: quit")
		response = raw_input("command: ")
		if response == "p":
			pen_num = int(raw_input("which pen? "))
			plotter.selectPen(pen_num)
		elif response == "s":
			char_height = float(raw_input("font height (in cm)? "))
			char_width = float(raw_input("font width (in cm)? "))
			plotter.write(SI(char_width, char_height))
		elif response == "q":
			finished = True
		else:
			plotter.write(LB("\n\r"))
	else:
		plotter.write(LB(line + "\n\r"))
	
print("l8r.")
