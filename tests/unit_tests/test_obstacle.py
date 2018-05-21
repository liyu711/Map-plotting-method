import unittest
from TranslationMethod import Obstacle
import numpy

class ObstacleTestCase(unittest.TestCase):
	
	def setUp(self):
		self.center_point1 = numpy.array([0,0,0])
		self.obstacle1 = Obstacle(2, self.center_point1)
		self.test_point1 = numpy.array([1,1,1])
		self.test_point2 = numpy.array([1,1,2])
		self.test_point3 = numpy.array([1,1,0])

	def test_ini(self):
		for point in self.obstacle1.boundary_points:
			print(point[0])
			print(point[1])
			print(point[2])

	def test_check_if_point_is_inside_the_obstacle(self):
		result1 = self.obstacle1.check_if_point_is_inside_the_obstacle(self.center_point1)
		result2 = self.obstacle1.check_if_point_is_inside_the_obstacle(self.test_point1)
		result3 = self.obstacle1.check_if_point_is_inside_the_obstacle(self.test_point2)
		result4 = self.obstacle1.check_if_point_is_inside_the_obstacle(self.test_point3)

		self.assertEqual(result1, True)
		self.assertEqual(result2, True)
		self.assertEqual(result3, False)
		self.assertEqual(result4, True)