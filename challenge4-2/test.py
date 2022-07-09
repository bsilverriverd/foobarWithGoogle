import unittest
from bringingAGunToATrainerFight import solution

class TestSolution(unittest.TestCase):
	def test_a(self):
		self.assertEqual(solution([3,2], [1,1], [2,1], 4), 7)
	
	def test_b(self):
		self.assertEqual(solution([300,275], [150,150], [185,100], 500), 9)
