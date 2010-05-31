from chiplotle import *
import random

number_of_points = 10
n_points_to_compute = 100

plotter = instantiate_plotters()[0]
left = plotter.margins.soft.left
right = plotter.margins.soft.right
bottom = plotter.margins.soft.bottom
top = plotter.margins.soft.top

plotter.select_pen(1)

points = []

for i in range(number_of_points):
	point_x = random.randint(left,right)
	point_y = random.randint(bottom,top)
	points.append((point_x,point_y))
	l = Label((point_x,point_y), i+1)
	plotter.write(l.format)

for point in points:
	c_1 = Cross(point,150,150)
	plotter.write(c_1.format)

catmull_curve = Catmull(points, points_to_compute = n_points_to_compute)
plotter.write(catmull_curve.format)

plotter.select_pen(0)
