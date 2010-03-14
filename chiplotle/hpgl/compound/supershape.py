from chiplotle.hpgl.compound.compound import _CompoundHPGL
from chiplotle.hpgl.commands import PU, PD, PA
from chiplotle.hpgl.scalable import Scalable
from chiplotle.utils.geometry import *
from chiplotle.tools.mathtools import superformula
from math import pi


class Supershape(_CompoundHPGL):
	'''Supershape, generated using the superformula
	first proposed by Johan Gielis.
	parameters are:
	w - width
	h - height
	a=b=1.0
	m, n1, n2, n3
	'''
	def __init__(self, xy, w, h, m, n1, n2, n3, points=1000, percentage=1.0, range=None):

		xy = xy or (0, 0)
		_CompoundHPGL.__init__(self, xy)
		self.width = Scalable(w)
		self.height = Scalable(h)
		self.m = m
		self.n1 = n1
		self.n2 = n2
		self.n3 = n3
		self.points = points
		self.percentage = percentage
		doublepi = pi * 2
		self.range = range or doublepi
		self.x, self.y = xy
		 
	@property
	def _subcommands(self):

		result = _CompoundHPGL._subcommands.fget(self)
		first = True
		for i in range(self.points):
			if i > self.points*self.percentage: 
				continue
			phi = i * self.range / self.points
			dx, dy = superformula(self.m, self.n1, self.n2, self.n3, phi)
			x = int((dx * self.width) + self.x)
			y = int((dy * self.height) + self.y)
			position = self.xyabsolute + (x, y)
			if first:
				result.append(PU( ))
				result.append(PA(position))
				result.append(PD( ))
				first = False
			else:
				result.append(PA(position))
		result.append(PU( ))
		
		return result		
