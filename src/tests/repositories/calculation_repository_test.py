import unittest
from services.calculation_service import CalculationService


class TestCalculationRepository(unittest.TestCase):
    def setUp(self):
        self.calculator = CalculationService()
        self.calculator.clear_all_calculations()

    def test_calculations_at_start(self):
        self.assertEqual(self.calculator.count(), 0)

    def test_no_calculations_at_start(self):
        self.assertEqual(self.calculator.get_last_result(),
                         "Memory is empty.\n")

    def test_none_calculations_at_start(self):
        self.assertEqual(self.calculator.return_calculations(), [])

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

    def test_calculations_clear_last_from_empty_memory(self):
        self.assertEqual(self.calculator.clear_last_calculation(),
                         "Error: Memory is empty.\n")

    def test_calculations_clear_last_two_in_memory(self):
        self.calculator.sqrt_service(2)
        self.calculator.exp_service(4, 5)
        self.assertEqual(self.calculator.clear_last_calculation(),
                         "Cleared last result from memory: 1024.\n")
        self.assertEqual(self.calculator.count(), 1)

    def test_calculations_clear_all_from_empty_memory(self):
        self.assertEqual(self.calculator.clear_all_calculations(),
                         "Error: Memory is empty.\n")

    def test_calculations_clear_all_two_in_memory(self):
        self.calculator.inv_service(2)
        self.calculator.exp_service(self.calculator.get_last_result(), 2)
        self.assertEqual(self.calculator.clear_all_calculations(),
                         "Cleared everything from memory.\n")

    def test_clear_all_from_memory(self):
        self.assertEqual(self.calculator.clear_all_calculations(), "Error: Memory is empty.\n")
