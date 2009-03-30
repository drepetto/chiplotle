import random, math

from chiplotle import *
from chiplotle.hpgl.compound import dorkbotfontdefs as font

class DorkbotFont():
	def __init__(self, outline_pen, fill_pen, outline_jitter, 
		fill_jitter, font_style, fill_style, x_char, cell_size):

		self.outline_pen = outline_pen
		self.fill_pen = fill_pen
		self.outline_jitter = outline_jitter
		self.fill_jitter = fill_jitter
		self.font_style = font_style
		self.fill_style = fill_style
		self.x_char = x_char
		self.cell_size = cell_size
		
	def plot(self, origin_x, origin_y, text):
		
		commands = []
		
		random.seed()
		
		#point_string = plotter.actualPosition
		#point_string_parts = point_string.split(',')
		#origin_x = int(point_string_parts[0])
		# the "- cell_size is there because rects are drawn from the bottom left
		# corner, but we've put our starting point at the top left
		#origin_y = int(point_string_parts[1]) - self.cell_size
		
		#plotter.write(SP(self.outline_pen))
		
		start_x = origin_x
		start_y = origin_y
		
		print("plotting text: \"" + text + "\" at starting point x: " + 
			str(start_x) + " y: " + str(start_y))
		
		# do outlines, if needed
		if self.fill_style < 3:
			commands.append(SP(self.outline_pen))
			#plotter.write(SP(self.outline_pen))
			
			for cur_char in text:
				character = font.char_dict[cur_char]
			
				cell_col = 0
				cell_row = 0
				
				while cell_row < 7:
				
					seg_num = cell_col + (cell_row * 3)
			
					if character[seg_num] == 1:
						jiggle_outline_x = math.floor(random.random() * self.outline_jitter * 
							self.cell_size) - (0.5 * self.outline_jitter * self.cell_size)
						jiggle_outline_y = math.floor(random.random() * self.outline_jitter * 
							self.cell_size) - (0.5 * self.outline_jitter * self.cell_size)
			
						x_outline = start_x + (cell_col * self.cell_size) + jiggle_outline_x
						y_outline = start_y - (cell_row * self.cell_size) + jiggle_outline_y
						
						if self.font_style == 1:				
							commands.append(PA([x_outline, y_outline]))
							commands.append(ER([self.cell_size,self.cell_size]))
							#plotter.goto(x_outline, y_outline)
							#plotter.write(ER([self.cell_size,self.cell_size]))
						elif self.font_style == 2:
							commands.append(PA([x_outline + self.cell_size/2, y_outline + self.cell_size/2]))
							commands.append(CI(self.cell_size/2))
							#plotter.goto(x_outline + self.cell_size/2, y_outline + self.cell_size/2)
							#plotter.write(CI(self.cell_size/2))
				
					cell_col = cell_col + 1
					if cell_col == 3:
						cell_col = 0
						cell_row = cell_row + 1
			
				start_x = start_x + (self.cell_size * 3) + (self.cell_size/2)
		
		
		
		# now do fills, if needed
		if self.fill_style == 1 or self.fill_style == 3:
		
			commands.append(SP(self.fill_pen))
			#plotter.write(SP(self.fill_pen))
			
			start_x = origin_x
			start_y = origin_y
			
			for cur_char in text:
				character = font.char_dict[cur_char]	
				cell_col = 0
				cell_row = 0
			
				while cell_row < 7:
				
					seg_num = cell_col + (cell_row * 3)
			
					if character[seg_num] == 1:
						jiggle_fill_x = math.floor(random.random() * self.fill_jitter * 
							self.cell_size) - (0.5 * self.fill_jitter * self.cell_size)
						jiggle_fill_y = math.floor(random.random() * self.fill_jitter * 
							self.cell_size) - (0.5 * self.fill_jitter * self.cell_size)
			
						x_fill = start_x + (cell_col * self.cell_size) + jiggle_fill_x
						y_fill = start_y - (cell_row * self.cell_size) + jiggle_fill_y
						
						if self.font_style == 1:
							commands.append(PA([x_fill, y_fill]))
							commands.append(RR([self.cell_size,self.cell_size]))
							#plotter.goto(x_fill, y_fill)
							#plotter.write(RR([self.cell_size,self.cell_size]))
						elif self.font_style == 2:
							commands.append(PA([x_fill + self.cell_size/2, y_fill + self.cell_size/2]))
							commands.append(WG(self.cell_size/2, 0, 360))
							#plotter.goto(x_fill + self.cell_size/2, y_fill + self.cell_size/2)
							#plotter.write(WG(self.cell_size/2, 0, 360))
				
					cell_col = cell_col + 1
					if cell_col == 3:
						cell_col = 0
						cell_row = cell_row + 1
			
				start_x = start_x + (self.cell_size * 3) + (self.cell_size/2)

		return commands
		
			
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
				
		
	
	
			
