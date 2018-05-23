import numpy
import math
from TranslationMethod import Map
from TranslationMethod import VectorMath
import random


class WorldGenerator(object):
	"""docstring for WorldGenerator"""
	def __init__(self):
		self.map_length = 0
		self.map_width = 0
		self.map_height = 0

	def generate_map(self, length, width, height, target_point):
		new_map = Map(length ,width, height, target_point)
		self.map_length = new_map.length
		self.map_width = new_map.width
		self.map_height = new_map.height

		return new_map

	
	def generate_obstacle(self, number_of_obstacles, map):
		loop_index = 0
		while loop_index < number_of_obstacles:
			min_value = VectorMath.get_the_least_value_from_three_numbers()
			side_length = random.uniform(0, min_value/2)
			center_point_x = random.uniform(map.special_boundary_points[0][0]+side_length, map.special_boundary_points[1][0]-side_length)
			center_point_y = random.uniform(map.special_boundary_points[0][1]+side_length, map.special_boundary_points[1][1]-side_length)
			center_point_z = random.uniform(map.special_boundary_points[0][2]+side_length, map.special_boundary_points[1][2]-side_length)
			obstacle = Obstacle(side_length, numpy.array([center_point_x, center_point_y, center_point_z]))