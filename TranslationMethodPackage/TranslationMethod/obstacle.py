import numpy

class Obstacle(object):
	"""docstring for Obstacle"""
	def __init__(self, side_length, center):
		# side_length: float
		# center: 3D array representing a point 
		self.side_length = side_length
		self.center = center
		self.boundary_points = [
			numpy.array([center[0]-side_length/2, center[1]-side_length/2, center[2]-side_length/2]),
			numpy.array([center[0]-side_length/2, center[1]-side_length/2, center[2]+side_length/2]),
			numpy.array([center[0]+side_length/2, center[1]-side_length/2, center[2]+side_length/2]),
			numpy.array([center[0]+side_length/2, center[1]-side_length/2, center[2]-side_length/2]),
			numpy.array([center[0]+side_length/2, center[1]+side_length/2, center[2]-side_length/2]),
			numpy.array([center[0]-side_length/2, center[1]+side_length/2, center[2]-side_length/2]),
			numpy.array([center[0]-side_length/2, center[1]+side_length/2, center[2]+side_length/2]),
			numpy.array([center[0]+side_length/2, center[1]+side_length/2, center[2]+side_length/2])
		]

	def get_side(self):
		return side_length

	def get_center(self):
		return center

	def check_if_point_is_inside_the_obstacle(self, point_to_check):
		status = False
		check_x = self.boundary_points[0][0] <= point_to_check[0] and point_to_check[0] <= self.boundary_points[7][0]
		check_y = self.boundary_points[0][1] <= point_to_check[1] and point_to_check[1] <= self.boundary_points[7][1]
		check_z = self.boundary_points[0][2] <= point_to_check[2] and point_to_check[2] <= self.boundary_points[7][2]
		if check_x and check_y and check_z:
			status = True

		return status
