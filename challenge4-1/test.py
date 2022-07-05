import unittest
from distractTheTrainers import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([1, 1]), 2)
	
	def test_b(self):
		self.assertEqual(solution([1, 7, 3, 21, 13, 19]), 0)
