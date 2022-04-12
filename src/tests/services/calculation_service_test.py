from services.calculation_service import CalculationService
import unittest


class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
        self.z = 4
        self.calculator = CalculationService()

    def test_sum_service_integer(self):
        self.assertEqual(self.calculator.sum_service(
            self.x, self.z), "2 + 4 = 6\n")

    def test_sum_service_float(self):
        self.assertEqual(self.calculator.sum_service(
            self.z, 1.313), "4 + 1.313 = 5.313\n")

    def test_sum_service_last(self):
        self.assertEqual(self.calculator.sum_service(
            -40.0, -2.0), "-40.0 + -2.0 = -42\n")

    def test_sub_service_integer(self):
        self.assertEqual(self.calculator.sub_service(
            self.x, self.z), "2 - 4 = -2\n")

    def test_sub_service_float(self):
        self.assertEqual(self.calculator.sub_service(
            self.y, 1.5), "3 - 1.5 = 1.5\n")

    def test_sub_service_last(self):
        self.assertEqual(self.calculator.sub_service(
            1.0, 2.0), "1.0 - 2.0 = -1\n")

    def test_mul_service_integer(self):
        self.assertEqual(self.calculator.mul_service(
            self.z, self.z), "4 * 4 = 16\n")

    def test_mul_service_float(self):
        self.assertEqual(self.calculator.mul_service(
            0.15, self.z), "0.15 * 4 = 0.6\n")

    def test_mul_service_last(self):
        self.assertEqual(self.calculator.mul_service(
            -3.0, self.y), "-3.0 * 3 = -9\n")

    def test_div_service_integer(self):
        self.assertEqual(self.calculator.div_service(
            self.x, self.x), "2 / 2 = 1\n")

    def test_div_service_float(self):
        self.assertEqual(self.calculator.div_service(
            self.x, self.z), "2 / 4 = 0.5\n")

    def test_div_service_last(self):
        self.assertEqual(self.calculator.div_service(
            12.0, self.z), "12.0 / 4 = 3\n")

    def test_div_service_last2(self):
        self.assertEqual(self.calculator.div_service(
            1, 100), "1 / 100 = 0.01\n")

    def test_div_service_zero_as_denominator(self):
        self.assertEqual(self.calculator.div_service(
            self.x, 0), "Division by Zero isn't allowed\n")

    def test_div_service_amounts_to_zero(self):
        self.assertEqual(self.calculator.div_service(
            0, self.x), "0 / 2 = 0\n")
