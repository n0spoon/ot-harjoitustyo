import math
from repositories.calculation_repository import CalculationRepository


class CalculationService:
    def __init__(self):
        self._calcdata = CalculationRepository()

    def string_to_number(self, var_s):
        var_i = var_s
        if var_i[0] == "-":
            var_i = var_i.lstrip("-")
        if "." in var_i:
            pieces = var_i.split(".")
            pieces_a = pieces[0]
            pieces_b = pieces[1]
            if (pieces_a.isnumeric() and pieces_b.isnumeric()) == False:
                return print(f"{var_s} is not a number")
        elif var_s.isnumeric() == False:
            return print(f"{var_s} is not a number")
        try:
            return int(str(var_s), 0)
        except ValueError:
            return float(var_s)

    def sum_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a+var_b)
        result = self.clean_result(result)
        self.add_result(result)
        return f"{var_a} + {var_b} = {result}\n"

    def sub_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a-var_b)
        result = self.clean_result(result)
        self.add_result(result)
        return f"{var_a} - {var_b} = {result}\n"

    def mul_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a*var_b)
        result = self.clean_result(result)
        self.add_result(result)
        return f"{var_a} * {var_b} = {result}\n"

    def div_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        if var_b == 0:
            return "Division by Zero isn't allowed\n"
        result = (var_a/var_b)
        result = self.clean_result(result)
        self.add_result(result)
        return f"{var_a} / {var_b} = {result}\n"

    def sqrt_service(self, var_a):
        var_a = self.string_to_number(var_a)
        if var_a < 0:
            return f"Error: Input number {var_a} is not a positive number\n"
        result = math.sqrt(var_a)
        result = f"±{self.clean_result(result)}"
        self.add_result(result)
        return f"√{var_a} = {result}\n"

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
