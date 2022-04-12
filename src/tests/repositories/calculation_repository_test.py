from services.calculation_service import CalculationService
import unittest


class TestCalculationRepository(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
        self.z = 4
        self.calculator = CalculationService()

    def test_calculations_at_start(self):
        self.assertEqual(self.calculator.count(), 0)

    def test_none_calculations_at_start(self):
        self.assertIsNone(self.calculator.return_calculations())

    def test_calculations_after_two_sum(self):
        self.calculator.sum_service("2", "3")
        self.calculator.sum_service(2.0, 3.5)
        self.assertEqual(self.calculator.count(), 2)

    def test_calculations_after_two_sub(self):
        self.calculator.sub_service("2", "3")
        self.calculator.sub_service(2.0, 3.5)
        self.assertEqual(self.calculator.count(), 2)
    
    def test_calculations_after_two_div(self):
        self.calculator.div_service("2", "3")
        self.calculator.div_service(2.0, 3.5)
        self.assertEqual(self.calculator.count(), 2)

    def test_calculations_after_two_mul(self):
        self.calculator.mul_service("2", "3")
        self.calculator.mul_service(2.0, 3.5)
        self.assertEqual(self.calculator.count(), 2)
