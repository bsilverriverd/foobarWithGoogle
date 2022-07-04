import unittest
from googleFooBar import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([13, 5, 6, 2, 5], [5, 2, 5, 13]), 6)
