import unittest
import numpy
import math
from TranslationMethodPackage.TranslationMethod import *

class TestVectorMath(unittest.TestCase):

	def setUp(self):
		self.center_point =  numpy.array([0,0,0])
		self.map = Map(100,100,100,self.center_point)

	def test_vector_norm(self):
		vector1 = numpy.array([1,1,1])
		vector2 = numpy.array([2,2,2])
		vector3 = [1,1,1]
