import numpy

class Map_in_3D(object):
	"""docstring for Map_in_3D"""
	def __init__(self, length, width, height, world_model):
		self.width = width
		self.length = length
		self.height = height
		self.boxy_map = numpy.ndarray(shape = (length, width, height), dtype = float)
		self.world_model = world_model
