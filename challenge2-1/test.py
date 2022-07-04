import unittest
from heyIAlreadyDidThat import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution('222', 3), 1)
