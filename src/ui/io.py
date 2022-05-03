from services.calculation_service import CalculationService


class IO:
    def __init__(self):
        self._calculator = CalculationService()
        self._commands = {
            "+": self._calculator.sum_service,
            "-": self._calculator.sub_service,
            "*": self._calculator.mul_service,
            "/": self._calculator.div_service,
            "?": self._calculator.count(),
            "sqrt": self._calculator.sqrt_service,
            "exp": self._calculator.exp_service,
            "inv": self._calculator.inv_service,
            "last": self._calculator.get_last_result,
        }
        self._guide = {
            1: "__________________________________________________________________\n",
            2: " Commands for Calculator:",
            3: " Enter + to sum two numbers",
            4: " Enter - to subtract latter number from the first",
            5: " Enter * to multiply two numbers",
            6: " Enter / to divide first number with the latter",
            7: " Enter sqrt to calculate square root of a positive number",
            8: " Enter exp to calculate value of first number raised into second",
            9: " Enter inv to calculate inverse value of a number",
            10: " Enter last instead of a number in calculation to use latest result",
            11: " Enter ? to get a count of calculations performed",
            12: " Enter x to stop",
            13: "__________________________________________________________________\n",
        }

    def start(self):
        self.print_guide()
        while True:
            command = input("Enter command: ")
            if command == "x":
                print(f"Exiting Calculator..\n")
                break
            if command == "?":
                print("Calculations:", self._calculator.count(), "\n")
                continue
            if command not in self._commands:
                print(f"Error: False Command {command}")
                self.print_guide()
                continue
            calculation = self._commands[command]
            if callable(calculation):
                if command == "sqrt" or command == "inv":
                    var_a = input("Enter a positive number: ")
                    if var_a == "last":
                        var_a = self._calculator.get_last_result()
                        if isinstance(var_a, str):
                            if (var_a[0] == "±"):
                                var_a = var_a.strip("±")
                                print(calculation("-" + var_a))
                                print(calculation(var_a))
                                continue
                    print(calculation(var_a))
                    continue
                if command == "last":
                    print("Error: Use last in a calculation\n")
                    continue
                var_a = input("Enter first number: ")
                var_b = input("Enter second number: ")
                if (var_a == "last") and (var_b == "last"):
                    var_a = self._calculator.get_last_result()
                    var_b = self._calculator.get_last_result()
                    if isinstance(var_a, str):
                        if var_a[0] == "±":
                            var_a = var_a.strip("±")
                            var_b = var_b.strip("±")
                            print(calculation("-" + var_a, var_b))
                            print(calculation(var_a, "-" + var_b))
                            print(calculation("-" + var_a, "-" + var_b))
                if var_a == "last":
                    var_a = self._calculator.get_last_result()
                    if isinstance(var_a, str):
                        if var_a[0] == "±":
                            var_a = var_a.strip("±")
                            print(calculation("-" + var_a, var_b))
                if var_b == "last":
                    var_b = self._calculator.get_last_result()
                    if isinstance(var_b, str):
                        if var_b[0] == "±":
                            var_b = var_b.strip("±")
                            print(calculation(var_a, "-" + var_b))
                print(calculation(var_a, var_b))

    def print_guide(self):
        return [print(value) for key, value in self._guide.items()]
