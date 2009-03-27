from chiplotle import *
from chiplotle.utils.run_chiplotle_UNIX import plotter

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

num_lines = len(from_address)
line_num = 0

while line_num < num_lines:
        line = from_address[line_num]
        plotter.write(LB(line))
        plotter.write(LB("\n\r"))
        line_num += 1

input = raw_input("\n\renter pen number for plotting TO ADDRESS:\n")
pen_num = int(input)

plotter.write(SP(pen_num))

raw_input("\n\rmove pen to top left of TO ADDRESS field and hit return to start plotting...")
print("plotting TO ADDRESS...")

num_lines = len(to_address)
line_num = 0

while line_num < num_lines:
	line = to_address[line_num]
	plotter.write(LB(line))
	plotter.write(LB("\n\r"))
	line_num += 1

plotter.write(SP(0))
print("done!")

