import unittest
from findTheAccessCodes import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([1,1,1]), 1)
	
	def test_b(self):
		self.assertEqual(solution([1,2,3,4,5,6]), 3)
