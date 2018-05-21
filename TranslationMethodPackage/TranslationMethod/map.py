import numpy
from TranslationMethod import *

class Map(object):
	"""docstring for Map_in_3D"""
	def __init__(self, length, width, height, target_point):
		self.width = width
		self.length = length
		self.height = height
		self.boxy_map = numpy.ndarray(shape = (length, width, height), dtype = float)
		self.target_point = target_point
