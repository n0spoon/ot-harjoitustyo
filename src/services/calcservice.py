class CalculatorService:
    def __init__(self):
        self._calculations = []

    def string_to_number(self, var_s):
        try:
            return int(str(var_s), 0)
        except:
            return float(var_s)

    def simple_sum(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        return var_a+var_b

    def sum_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a+var_b)
        pieces = str(result).split(".")
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        self._calculations.append(result)
        return f"{var_a} + {var_b} = {result}\n"

    def sub_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a-var_b)
        pieces = str(result).split(".")
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        self._calculations.append(result)
        return f"{var_a} - {var_b} = {result}\n"

    def mul_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        result = (var_a*var_b)
        pieces = str(result).split(("."))
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        self._calculations.append(result)
        return f"{var_a} * {var_b} = {result}\n"

    def div_service(self, var_a, var_b):
        var_a = self.string_to_number(var_a)
        var_b = self.string_to_number(var_b)
        if var_b == 0:
            return "Division by Zero isn't allowed\n"
        result = (var_a/var_b)
        pieces = str(result).split(("."))
        if len(pieces[-1]) == 1:
            last = int(pieces[-1])
            if last == 0:
                result = int(result)
        self._calculations.append(result)
        return f"{var_a} / {var_b} = {result}\n"

    def calculations(self):
        return len(self._calculations)
