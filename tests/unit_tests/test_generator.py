import unittest
import numpy
from TranslationMethod import *

class WorldGeneratorTestCase(unittest.TestCase):
	"""docstring for WorldGeneratorTestCase"""
	def setUp(self):
		self.generator = WorldGenerator()
		self.target_point = numpy.array([25,25,0])

	def test_generate_map(self):
		map = self.generator.generate_map(100, 100, 100, self.target_point)
		self.assertEqual(100, map.length)
		self.assertEqual(100, map.height)
		self.assertEqual(100, map.width)
		self.assertEqual(self.target_point[0], map.target_point[0])
		self.assertEqual(self.target_point[1], map.target_point[1])
		self.assertEqual(self.target_point[2], map.target_point[2])
