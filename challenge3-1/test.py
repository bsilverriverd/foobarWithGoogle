import unittest
from prepareTheBunniesEscape import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]), 7)
	
	def test_b(self):
		self.assertEqual(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]), 11)

	def test_c(self):
		self.assertEqual(solution([[0, 1, 0, 0], [1, 1, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0], [0, 1, 1, 1], [0, 0, 0, 0]]), 15)

	def test_d(self):
		self.assertEqual(solution([[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]), 9)

	def test_e(self):
		self.assertEqual(solution([[0,0,0,0,0,1,1,0,0,0],[1,1,0,1,0,1,1,0,1,0],[0,0,0,0,0,0,0,0,1,0],[1,1,1,1,1,1,1,1,1,0],[1,1,1,1,0,0,0,0,0,0]]), 14)

	def test_f(self):
		self.assertEqual(solution([[0,1,0,0,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,1,0,1,0,1,0,0],[0,0,0,1,0,1,0,0]]), 29)
