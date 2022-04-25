from repositories.calculation_repository import CalculationRepository


class CalculationService:
    def __init__(self):
        self._calcdata = CalculationRepository()

    def string_to_number(self, var_s):
        try:
            return int(str(var_s), 0)
        except ValueError:
            try:
                return float(var_s)
            except ValueError:
                return print(f"Error: {var_s} is not a number")

    def sum_service(self, var_a, var_b):
        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x+var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} + {var_y} = {result}\n"
        except TypeError:
            return ""

    def sub_service(self, var_a, var_b):
        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x-var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} - {var_y} = {result}\n"
        except TypeError:
            return ""

    def mul_service(self, var_a, var_b):
        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            result = (var_x*var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} * {var_y} = {result}\n"
        except TypeError:
            return ""

    def div_service(self, var_a, var_b):
        try:
            var_x = self.string_to_number(var_a)
            var_y = self.string_to_number(var_b)
            if var_y == 0:
                return "Division by Zero isn't allowed\n"
            result = (var_x/var_y)
            result = self.clean_result(result)
            self.add_result(result)
            return f"{var_x} / {var_y} = {result}\n"
        except TypeError:
            return ""

    def sqrt_service(self, var_a):
        try:
            var_x = self.string_to_number(var_a)
            if var_x < 0:
                return f"Error: Input {var_x} is not a positive number\n"
            result = var_x**(1/2)
            result = f"±{self.clean_result(result)}"
            self.add_result(result)
            return f"√{var_x} = {result}\n"
        except TypeError:
            return ""

    def clean_result(self, result):
        pieces = str(result).split(".")
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        return result

    def count(self):
        return self._calcdata.count_calculations()

    def return_calculations(self):
        return self._calcdata.print_calculations()

    def add_result(self, result):
        self._calcdata.add_calculation(result)
