from chiplotle.utils.run_chiplotle_UNIX import plotter
from chiplotle import MayaNumber
from chiplotle.hpgl.compound.dorkbotfont import DorkbotFont



def main():
	
	print("*********************")
	print("* DORKBOT FONT TEST *")
	print("*********************")
	
	input = raw_input("enter font outline pen number:")
	outline_pen = int(input)
	input = raw_input("enter font fill pen number:")
	fill_pen = int(input)
	input = raw_input("enter font outline jitter (0-100):")
	outline_jitter = int(input) / 100.0
	input = raw_input("enter font fill jitter (0-100):")
	fill_jitter = int(input) / 100.0
	input = raw_input("enter font style (1 = rects, 2 = circles, 3 = Xs):")
	font_style = int(input)
	
	x_char = 'x'
	
	if font_style < 3:
		fill_style = int(raw_input(
			"enter fill style (1 = outline + fill, 2 = outline only, 3 = fill only):"))
	elif font_style == 3:
		x_char = raw_input("enter character to use for Xs:")
		fill_style = 4
	
	input = raw_input("enter font cell size in plotter points:")
	cell_size = int(input)
	
	font = DorkbotFont(outline_pen,fill_pen,outline_jitter,fill_jitter,font_style,
		fill_style,x_char,cell_size)
	
	finished = False
	
	while finished == False:	
		text = raw_input("enter text to plot (blank line to end):")

		if len(text) == 0:
			finished = True
		else:
			input = raw_input("move to top left corner and hit enter to begin plotting...")
			font.plot(text)

	plotter.penUp()

if __name__ == '__main__': main()

