import unittest
from services.calculation_service import CalculationService


class TestCalculatorService(unittest.TestCase):
    def setUp(self):
        self.x = 2
        self.y = 3
        self.z = 4
        self.calculator = CalculationService()
        self.calculator.clear_all_calculations()

    def tearDown(self):
        self.calculator.clear_all_calculations()

    def test_string_to_number_input_error(self):
        self.assertEqual(self.calculator.string_to_number("456.kek"), None)

    def test_string_to_number_input_success_integer(self):
        self.assertEqual(self.calculator.string_to_number("123456"), 123456)

    def test_string_to_number_input_success_float(self):
        self.assertEqual(self.calculator.string_to_number("123.456"), 123.456)

    def test_string_to_number_nan_input(self):
        self.assertIsNone(self.calculator.string_to_number("NaN"))

    def test_sum_service_integer(self):
        self.assertEqual(self.calculator.sum_service(
            self.x, self.z), "2 + 4 = 6\n")

    def test_sum_service_float(self):
        self.assertEqual(self.calculator.sum_service(
            self.z, 1.313), "4 + 1.313 = 5.313\n")

    def test_sum_service_last(self):
        self.assertEqual(self.calculator.sum_service(
            -40.0, -2.0), "-40.0 + -2.0 = -42\n")

    def test_sum_service_invalid_input(self):
        self.assertEqual(self.calculator.sum_service(
            "tjt.234", "123.ke9?"), "")

    def test_sum_service_nan_input(self):
        self.calculator.sum_service(float("NaN"), 42)
        self.assertEqual(self.calculator.count(), 0)

    def test_sum_service_nan_output(self):
        self.assertEqual(self.calculator.sum_service(
            "inf", "-inf"), "inf + -inf = nan\n")
        self.assertEqual(self.calculator.count(), 0)

    def test_sub_service_integer(self):
        self.assertEqual(self.calculator.sub_service(
            self.x, self.z), "2 - 4 = -2\n")

    def test_sub_service_float(self):
        self.assertEqual(self.calculator.sub_service(
            self.y, 1.5), "3 - 1.5 = 1.5\n")

    def test_sub_service_last(self):
        self.assertEqual(self.calculator.sub_service(
            1.0, 2.0), "1.0 - 2.0 = -1\n")

    def test_sub_service_invalid_input(self):
        self.assertEqual(self.calculator.sub_service(
            "errorsana", "123.yep"), "")

    def test_sub_service_nan_input(self):
        self.calculator.sub_service(983745.23, float("Nan"))
        self.assertEqual(self.calculator.count(), 0)

    def test_sub_service_nan_output(self):
        self.assertEqual(self.calculator.sub_service(
            "inf", "inf"), "inf - inf = nan\n")
        self.assertEqual(self.calculator.count(), 0)

    def test_mul_service_integer(self):
        self.assertEqual(self.calculator.mul_service(
            self.z, self.z), "4 * 4 = 16\n")

    def test_mul_service_float(self):
        self.assertEqual(self.calculator.mul_service(
            0.15, self.z), "0.15 * 4 = 0.6\n")

    def test_mul_service_last(self):
        self.assertEqual(self.calculator.mul_service(
            -3.0, self.y), "-3.0 * 3 = -9\n")

    def test_mul_service_invalid_input(self):
        self.assertEqual(self.calculator.mul_service("jih.959", "ierj"), "")

    def test_mul_service_nan_input(self):
        self.calculator.mul_service(float("naN"), 0.123678)
        self.assertEqual(self.calculator.count(), 0)

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
            self.x, 0), "Error: Division by Zero isn't allowed\n")

    def test_div_service_amounts_to_zero(self):
        self.assertEqual(self.calculator.div_service(
            0, self.x), "0 / 2 = 0\n")

    def test_div_service_invalid_input(self):
        self.assertEqual(self.calculator.div_service("123.yep", 313), "")

    def test_div_service_nan_input(self):
        self.calculator.div_service(0.0932486723, float("nAN"))
        self.assertEqual(self.calculator.count(), 0)

    def test_div_service_nan_output(self):
        self.assertEqual(self.calculator.div_service(
            "-inf", "-inf"), "-inf / -inf = nan\n")
        self.assertEqual(self.calculator.count(), 0)

    def test_sqrt_service_negative_input(self):
        self.assertEqual(self.calculator.sqrt_service(-1),
                         "Error: Input -1 is not a positive number\n")

    def test_sqrt_service_integer(self):
        self.assertEqual(self.calculator.sqrt_service(
            self.z), f"√{self.z} = ±{self.x}\n")

    def test_sqrt_service_float(self):
        self.assertEqual(self.calculator.sqrt_service(0.25), f"√0.25 = ±0.5\n")

    def test_sqrt_service_invalid_input_error(self):
        self.assertEqual(self.calculator.sqrt_service("123.yep"), "")

    def test_sqrt_service_nan_input(self):
        self.calculator.sqrt_service(float("NaN"))
        self.assertEqual(self.calculator.count(), 0)

    def test_exp_service_integer(self):
        self.assertEqual(self.calculator.exp_service(
            5, 8), "5^8 = 390625\n")

    def test_exp_service_float(self):
        self.assertEqual(self.calculator.exp_service(
            0.5, self.y), "0.5^3 = 0.125\n")

    def test_exp_service_negative_exponent(self):
        self.assertEqual(self.calculator.exp_service(
            self.z, -0.5), "4^-0.5 = 0.5\n")

    def test_exp_service_division_by_zero(self):
        self.assertEqual(self.calculator.exp_service(
            0.0, -12), "Error: Division by Zero isn't allowed\n")

    def test_exp_service_as_sqrt(self):
        self.assertEqual(self.calculator.exp_service(
            2, 0.5), "2^0.5 = ±1.4142135623730951\n")

    def test_exp_service_invalid_input(self):
        self.assertEqual(self.calculator.exp_service(
            0.69, "nopers"), "")

    def test_exp_service_nan_input(self):
        self.calculator.exp_service(908569.5783, float("nan"))
        self.assertEqual(self.calculator.count(), 0)

    def test_inv_service_integer(self):
        self.assertEqual(self.calculator.inv_service(
            1), "1 / 1 = 1\n")

    def test_inv_service_float(self):
        self.assertEqual(self.calculator.inv_service(
            100), "1 / 100 = 0.01\n")

    def test_inv_service_negative(self):
        self.assertEqual(self.calculator.inv_service(
            -2), "1 / -2 = -0.5\n")

    def test_inv_service_division_by_zero(self):
        self.assertEqual(self.calculator.inv_service(
            0), "Error: Division by Zero isn't allowed\n")

    def test_inv_service_invalid_input(self):
        self.assertEqual(self.calculator.inv_service(
            "failings"), "")

    def test_inv_service_nan_input(self):
        self.calculator.inv_service(float("NaN"))
        self.assertEqual(self.calculator.count(), 0)

    def test_ceil_service_pi(self):
        self.assertEqual(self.calculator.ceil_service(
            self.calculator.constant_pi()
        ), "The ceiling value of 3.141592653589793 = 4\n")

    def test_ceil_service_neper(self):
        self.assertEqual(self.calculator.ceil_service(
            self.calculator.constant_e()
        ), "The ceiling value of 2.718281828459045 = 3\n")

    def test_ceil_service_invalid_input(self):
        self.assertEqual(self.calculator.ceil_service(
            "asdasd.0974"), "")

    def test_ceil_service_nan_input(self):
        self.calculator.ceil_service(float("NaN"))
        self.assertEqual(self.calculator.count(), 0)

    def test_ceil_service_inf_input(self):
        self.assertEqual(self.calculator.ceil_service(
            "inf"), "The ceiling value of inf = inf\n")
        self.assertEqual(self.calculator.count(), 1)

    def test_ceil_service_neg_inf_input(self):
        self.assertEqual(self.calculator.ceil_service(
            "-inf"), "The ceiling value of -inf = -inf\n")
        self.assertEqual(self.calculator.count(), 1)

    def test_floor_service_pi(self):
        self.assertEqual(self.calculator.floor_service(
            self.calculator.constant_pi()
        ), "The floor value of 3.141592653589793 = 3\n")

    def test_floor_service_neper(self):
        self.assertEqual(self.calculator.floor_service(
            self.calculator.constant_e()
        ), "The floor value of 2.718281828459045 = 2\n")

    def test_floor_service_invalid_input(self):
        self.assertEqual(self.calculator.floor_service(
            "yepep.5678"), "")

    def test_floor_service_nan_input(self):
        self.calculator.floor_service(float("nan"))
        self.assertEqual(self.calculator.count(), 0)

    def test_floor_service_inf_input(self):
        self.assertEqual(self.calculator.floor_service(
            "inf"), "The floor value of inf = inf\n")
        self.assertEqual(self.calculator.count(), 1)

    def test_floor_service_neg_inf_input(self):
        self.assertEqual(self.calculator.floor_service(
            "-inf"), "The floor value of -inf = -inf\n")
        self.assertEqual(self.calculator.count(), 1)
