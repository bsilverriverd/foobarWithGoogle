import unittest
from distractTheTrainers import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([1, 1]), 2)
	
	def test_b(self):
		self.assertEqual(solution([1, 7, 3, 21, 13, 19]), 0)

	def test_c(self):
		self.assertEqual(solution([3, 21, 3]), 3)

	def test_d(self):
		self.assertEqual(solution([1, 23, 1]), 1)
	
	def test_e(self):
		self.assertEqual(solution([1, 7, 3, 21, 13, 19, 1, 19]), 0)
	
	def test_f(self):
		self.assertEqual(solution([1, 3, 21]), 1)
