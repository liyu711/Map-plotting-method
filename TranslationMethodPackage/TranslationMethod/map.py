import numpy
from TranslationMethod import *

class Map(object):
	"""docstring for Map_in_3D"""
	def __init__(self, length, width, height, target_point):
		# center is always[0,0,0]
		# length, width, height represents x, y, z
		self.width = width
		self.length = length
		self.height = height
		self.box = numpy.ndarray(shape = (length, width, height), dtype = float)
		self.target_point = target_point
		self.obstacles = numpy.array([])
		self.special_boundary_points = [
			numpy.array([-self.length/2, -self.width/2, -self.height/2]),
			numpy.array([self.length/2, self.width/2, self.height/2])
		]

	def add_obstacle(self, obstacle):
		self.obstacles = numpy.hstack([self.obstacles, obstacle])

	def reset_obstacles(self):
		self.obstacles = []

	def add_obstacles(self, obstacles):
		for obstacle in obstacles:
			self.add_obstacle(obstacle)	