import unittest
from powerHungry import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([1,1,1]), '1')
	
	def test_b(self):
		self.assertEqual(solution([1,2,3,4,5,6]), '720')

	def test_c(self):
		self.assertEqual(solution([-2, -3, 4, -5]), '60')
