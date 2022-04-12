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
        }
        self._guide = {
            1: "__________________________________________________",
            2: "Commands for Calculator:",
            3: "Enter + to sum two numbers",
            4: "Enter - to subtract latter number from the first",
            5: "Enter * to multiply two numbers",
            6: "Enter / to divide first number with the latter",
            7: "Enter ? to get a count of calculations performed",
            8: "Enter x to stop",
            9: "__________________________________________________\n",
        }

    def start(self):
        self.print_guide()
        while True:
            command = input("Enter command: ")
            if command == "x":
                break
            if command == "?":
                print("Calculations:", self._calculator.count(), "\n")
                continue
            if command not in self._commands:
                print("Error: False Command")
                self.print_guide()
                continue
            var_a = input("Enter first number: ")
            var_b = input("Enter second number: ")
            calculation = self._commands[command]
            if callable(calculation):
                print(calculation(var_a, var_b))

    def print_guide(self):
        return [print(value) for key, value in self._guide.items()]
