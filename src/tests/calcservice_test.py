from services.calcservice import CalculatorService
from ui.iface import IO
import unittest

class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
        self.z = 4
        self.calculator = CalculatorService()

    def test_calculationsAtStart(self):
        self.assertEqual(self.calculator.calculations(), 0)

    def test_simpleSum(self):
        self.assertEqual(self.calculator.simpleSum(self.x, self.z), 6)
    
    def test_sumServiceInteger(self):
        self.assertEqual(self.calculator.sumService(self.x, self.z), "2 + 4 = 6")
    
    def test_sumServiceFloat(self):
        self.assertEqual(self.calculator.sumService(self.z, 1.313), "4 + 1.313 = 5.313")
    
    def test_subServiceInteger(self):
        self.assertEqual(self.calculator.subService(self.x, self.z), "2 - 4 = -2")
    
    def test_subServiceFloat(self):
        self.assertEqual(self.calculator.subService(self.y, 1.5), "3 - 1.5 = 1.5")