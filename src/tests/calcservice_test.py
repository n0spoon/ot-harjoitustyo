from services.calcservice import CalculatorService
from ui.iface import IO
import unittest

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 4
        self.calculator = CalculatorService()

    def test_calculationsAtStart(self):
        self.assertEqual(self.calculator.calculations(), 0)

    def test_simpleSum(self):
        self.assertEqual(self.calculator.simpleSum(self.x, self.y), 6)