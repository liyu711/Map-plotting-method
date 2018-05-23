import unittest
import numpy
from TranslationMethod import *

class WorldGeneratorTestCase(unittest.TestCase):
	"""docstring for WorldGeneratorTestCase"""
	def setUp(self):
		self.generator = WorldGenerator()
		self.target_point = numpy.array([25,25,0])

	def test_generate_map(self):
		self.generator.reset_value()
		map1 = self.generator.generate_map(100, 100, 100, self.target_point)
		self.assertEqual(100, map1.length)
		self.assertEqual(100, map1.height)
		self.assertEqual(100, map1.width)
		self.assertEqual(self.target_point[0], map1.target_point[0])
		self.assertEqual(self.target_point[1], map1.target_point[1])
		self.assertEqual(self.target_point[2], map1.target_point[2])

	def test_generate_obstacle(self):
		self.generator.reset_value()
		map1 = self.generator.generate_map(100, 50, 50, self.target_point)
		list_of_obstacles = self.generator.generate_obstacle(1000, map1)
		for obstacle in list_of_obstacles:
			self.assertEqual(obstacle.side_length <25, True)
			self.assertEqual(obstacle.center[0] > (-50+obstacle.side_length) and obstacle.center[0] < (50-obstacle.side_length), True)
			self.assertEqual(obstacle.center[1] > (-25+obstacle.side_length) and obstacle.center[1] < (25-obstacle.side_length), True)
			self.assertEqual(obstacle.center[2] > (-25+obstacle.side_length) and obstacle.center[2] < (25-obstacle.side_length), True)

		map2 = self.generator.generate_map(200, 150, 60, self.target_point)
		list_of_obstacles2 = self.generator.generate_obstacle(1000, map2)
		for obstacle in list_of_obstacles2:
			self.assertEqual(obstacle.side_length <30, True)
			self.assertEqual(obstacle.center[0] > (-100+obstacle.side_length) and obstacle.center[0] < (100-obstacle.side_length), True)
			self.assertEqual(obstacle.center[1] > (-75+obstacle.side_length) and obstacle.center[1] < (75-obstacle.side_length), True)
			self.assertEqual(obstacle.center[2] > (-30+obstacle.side_length) and obstacle.center[2] < (30-obstacle.side_length), True)
