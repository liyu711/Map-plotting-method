import math
import numpy

class VectorMath(object):

	def __init__(self):
		pass

	@staticmethod
	def get_magnitude(vector1, vector2):
		# vector1 is the initial point
		# vector2 is the point you want to reach
		difference = numpy.subtract(vector2, vector1)
		magnitude = numpy.linalg.norm(difference)

		return magnitude

	@staticmethod
	def get_single_magnitude(vector):
		magnitude = numpy.linalg.norm(vector)

		return magnitude

	@staticmethod
	def get_the_least_value_from_three_numbers( one, two, three):
		min_value = 99999999999999999
		if one < min_value:
			min_value = one
			if two < min_value:
				min_value = two
				if three < min_value:
					min_value = three

		return min_value


