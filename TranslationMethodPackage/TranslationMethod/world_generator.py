import numpy
import math
from TranslationMethod import Map
from TranslationMethod import VectorMath
from TranslationMethod import Obstacle
import random


class WorldGenerator(object):
	"""docstring for WorldGenerator"""
	def __init__(self):
		self.map_length = 0
		self.map_width = 0
		self.map_height = 0

	def reset_value(self):
		self.map_length = 0
		self.map_width = 0
		self.map_height = 0

	def generate_map(self, length, width, height, target_point):
		new_map = Map(length ,width, height, target_point)
		self.map_length = new_map.length
		self.map_width = new_map.width
		self.map_height = new_map.height

		return new_map

	def generate_obstacle(self, number_of_obstacles, map_1):
		loop_index = 0
		list_of_obstacles = []
		while loop_index < number_of_obstacles:
			min_value = VectorMath.get_the_least_value_from_three_numbers(map_1.length, map_1.width, map_1.height)
			side_length = random.uniform(0, min_value/2)
			center_point_x = random.uniform(map_1.special_boundary_points[0][0]+side_length, map_1.special_boundary_points[1][0]-side_length)
			center_point_y = random.uniform(map_1.special_boundary_points[0][1]+side_length, map_1.special_boundary_points[1][1]-side_length)
			center_point_z = random.uniform(map_1.special_boundary_points[0][2]+side_length, map_1.special_boundary_points[1][2]-side_length)
			obstacle = Obstacle(side_length, numpy.array([center_point_x, center_point_y, center_point_z]))
			list_of_obstacles.append(obstacle)
			loop_index += 1
		
		return list_of_obstacles