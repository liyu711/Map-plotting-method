import numpy
import math
from TranslationMethod import Map

class WorldGenerator(object):
	"""docstring for WorldGenerator"""
	def __init__(self):
		pass

	def generate_map(self, length, width, height, target_point):
		new_map = Map(length ,width, height, target_point)
		return new_map
	
	def generate_obstacle(self):
		
		
		
		