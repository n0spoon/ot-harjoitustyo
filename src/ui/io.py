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
            9: " Enter ? to get a count of calculations performed",
            10: " Enter x to stop",
            11: "__________________________________________________________________\n",
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
            if command == "sqrt":
                var_a = input("Enter a positive number: ")
                calculation = self._commands[command]
                if callable(calculation):
                    print(calculation(var_a))
                    continue
            var_a = input("Enter first number: ")
            var_b = input("Enter second number: ")
            calculation = self._commands[command]
            if callable(calculation):
                print(calculation(var_a, var_b))

    def print_guide(self):
        return [print(value) for key, value in self._guide.items()]
