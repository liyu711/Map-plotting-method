import numpy
from TranslationMethod import VectorMath

class Obstacle(object):
	"""docstring for Obstacle"""
	def __init__(self, side_length, center):
		# side_length: float
		# center: 3D array representing a point 
		self.side_length = side_length
		self.center = center
		self.current_point = center
		self.current_point = center
		self.boundary_points = [
			numpy.array([self.center[0]-side_length/2, self.center[1]-side_length/2, self.center[2]-side_length/2]),
			numpy.array([self.center[0]-side_length/2, self.center[1]-side_length/2, self.center[2]+side_length/2]),
			numpy.array([self.center[0]+side_length/2, self.center[1]-side_length/2, self.center[2]+side_length/2]),
			numpy.array([self.center[0]+side_length/2, self.center[1]-side_length/2, self.center[2]-side_length/2]),
			numpy.array([self.center[0]+side_length/2, self.center[1]+side_length/2, self.center[2]-side_length/2]),
			numpy.array([self.center[0]-side_length/2, self.center[1]+side_length/2, self.center[2]-side_length/2]),
			numpy.array([self.center[0]-side_length/2, self.center[1]+side_length/2, self.center[2]+side_length/2]),
			numpy.array([self.center[0]+side_length/2, self.center[1]+side_length/2, self.center[2]+side_length/2])
		]
		self.attempted_path = [
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0], self.center[1], self.center[2]-1]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]+1]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]+1]),
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]+1]),
			numpy.array([self.center[0], self.center[1], self.center[2]+1]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]+1])
		]

	def reset_attempted_path(self):
		self.attempted_path = [
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0], self.center[1], self.center[2]-1]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]-1]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]-1]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]]),
			numpy.array([self.center[0]-1, self.center[1]+1, self.center[2]+1]),
			numpy.array([self.center[0]-1, self.center[1], self.center[2]+1]),
			numpy.array([self.center[0]-1, self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0], self.center[1]+1, self.center[2]+1]),
			numpy.array([self.center[0], self.center[1], self.center[2]+1]),
			numpy.array([self.center[0], self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1]-1, self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1], self.center[2]+1]),
			numpy.array([self.center[0]+1, self.center[1]+1, self.center[2]+1])
		]

	def update_attempted_path(self):
		self.attempted_path = [
			numpy.array([self.current_point[0]-1, self.current_point[1]-1, self.current_point[2]-1]),
			numpy.array([self.current_point[0]-1, self.current_point[1], self.current_point[2]-1]),
			numpy.array([self.current_point[0]-1, self.current_point[1]+1, self.current_point[2]-1]),
			numpy.array([self.current_point[0], self.current_point[1]+1, self.current_point[2]-1]),
			numpy.array([self.current_point[0], self.current_point[1], self.current_point[2]-1]),
			numpy.array([self.current_point[0], self.current_point[1]-1, self.current_point[2]-1]),
			numpy.array([self.current_point[0]+1, self.current_point[1]+1, self.current_point[2]-1]),
			numpy.array([self.current_point[0]+1, self.current_point[1], self.current_point[2]-1]),
			numpy.array([self.current_point[0]+1, self.current_point[1]-1, self.current_point[2]-1]),
			numpy.array([self.current_point[0]-1, self.current_point[1]+1, self.current_point[2]]),
			numpy.array([self.current_point[0]-1, self.current_point[1], self.current_point[2]]),
			numpy.array([self.current_point[0]-1, self.current_point[1]-1, self.current_point[2]]),
			numpy.array([self.current_point[0], self.current_point[1]+1, self.current_point[2]]),
			numpy.array([self.current_point[0], self.current_point[1]-1, self.current_point[2]]),
			numpy.array([self.current_point[0]+1, self.current_point[1]+1, self.current_point[2]]),
			numpy.array([self.current_point[0]+1, self.current_point[1], self.current_point[2]]),
			numpy.array([self.current_point[0]+1, self.current_point[1]-1, self.current_point[2]]),
			numpy.array([self.current_point[0]-1, self.current_point[1]+1, self.current_point[2]+1]),
			numpy.array([self.current_point[0]-1, self.current_point[1], self.current_point[2]+1]),
			numpy.array([self.current_point[0]-1, self.current_point[1]-1, self.current_point[2]+1]),
			numpy.array([self.current_point[0], self.current_point[1]+1, self.current_point[2]+1]),
			numpy.array([self.current_point[0], self.current_point[1], self.current_point[2]+1]),
			numpy.array([self.current_point[0], self.current_point[1]-1, self.current_point[2]+1]),
			numpy.array([self.current_point[0]+1, self.current_point[1]-1, self.current_point[2]+1]),
			numpy.array([self.current_point[0]+1, self.current_point[1], self.current_point[2]+1]),
			numpy.array([self.current_point[0]+1, self.current_point[1]+1, self.current_point[2]+1])
		]

	def get_cubic_value_for_plotting(self, current_map):
		x, y, z = numpy.indices((current_map.length, current_map.width, current_map.height))
		cubic_value = (x > self.boundary_points[0][0]) & (x < self.boundary_points[7][0]) & (y > self.boundary_points[0][1]) & (y < self.boundary_points[7][1]) & (z > self.boundary_points[0][2]) & (z < self.boundary_points[7][2])

		return cubic_value

	def get_side(self):
		return self.side_length

	def get_center(self):
		return self.center

	def get_current_point(self):
		return self.current_point

	def set_current_point(self, point):
		self.current_point = point

	def reset_current_point(self):
		self.current_point = self.center

	def check_if_point_is_inside_the_obstacle(self, point_to_check):
		status = False
		check_x = self.boundary_points[0][0] <= point_to_check[0] and point_to_check[0] <= self.boundary_points[7][0]
		check_y = self.boundary_points[0][1] <= point_to_check[1] and point_to_check[1] <= self.boundary_points[7][1]
		check_z = self.boundary_points[0][2] <= point_to_check[2] and point_to_check[2] <= self.boundary_points[7][2]
		if check_x and check_y and check_z:
			status = True

		return status

	def filtering_path(self, obstacle):
		# self adjusting its attempted path according to obstacle
		loop_index = 0
		while loop_index < len(self.attempted_path):
			check_status = obstacle.check_if_point_is_inside_the_obstacle(self.attempted_path[loop_index])
			if check_status:
				del self.attempted_path[loop_index]
				loop_index -= 1
			loop_index += 1

	def move(self, fin_point):
		min_magnitude = 10000000000000
		point_to_go = self.current_point

		for point in self.attempted_path:
			distance_magnitude_to_the_end = VectorMath.get_magnitude(fin_point, point)
			if distance_magnitude_to_the_end < min_magnitude:
				min_magnitude = distance_magnitude_to_the_end
				point_to_go = point

		self.set_current_point(point_to_go)
		self.update_attempted_path()