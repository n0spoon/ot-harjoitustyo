from services.calculation_service import CalculationService
import unittest


class TestCalculationRepository(unittest.TestCase):
    def setUp(self):
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

    def test_calculations_after_two_sqrt(self):
        self.calculator.sqrt_service("4")
        self.calculator.sqrt_service(4)
        self.assertEqual(self.calculator.count(), 2)

    def test_calculations_after_error_sum(self):
        self.calculator.sum_service("lkl.840", 99)
        self.assertEqual(self.calculator.count(), 0)

    def test_calculations_after_error_sub(self):
        self.calculator.sub_service("iuh.457", 13)
        self.assertEqual(self.calculator.count(), 0)

    def test_calculations_after_error_div(self):
        self.calculator.div_service("987.ijkl", 313)
        self.assertEqual(self.calculator.count(), 0)

    def test_calculations_after_error_mul(self):
        self.calculator.mul_service("456.oij", 42)
        self.assertEqual(self.calculator.count(), 0)

    def test_calculations_after_error_sqrt(self):
        self.calculator.sqrt_service("yep.123")
        self.assertEqual(self.calculator.count(), 0)

    def test_calculations_get_last_result_sqrt(self):
        self.calculator.mul_service(6, 6)
        self.assertEqual(self.calculator.sqrt_service(
            self.calculator.get_last_result()), "√36 = ±6\n")

    def test_calculations_get_last_result_plusminus(self):
        self.calculator.sqrt_service(4)
        var_a = self.calculator.get_last_result()
        self.assertEqual(var_a, "±2")

#    def test_calculations_get_last_result_none(self):
#        self.assertEqual(self.calculator.sum_service(
#            self.calculator.get_last_result(), 1), "Error: Memory is empty\")
#        self.assertEqual(self.calculator.count(), 0)
