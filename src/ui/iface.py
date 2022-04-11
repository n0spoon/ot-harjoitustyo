from services.calcservice import CalculatorService


class IO:
    def __init__(self):
        self.calculator = CalculatorService()
        self._commands = {
            "+": self.calculator.sum_service,
            "-": self.calculator.sub_service,
            "*": self.calculator.mul_service,
            "/": self.calculator.div_service,
        }

    def start(self):
        self.print_guide()
        while True:
            command = input("Enter command: ")
            if command == "x":
                break
            if command not in self._commands:
                print("Error: False Command")
                self.print_guide()
                continue
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            calculation = self._commands[command]
            if callable(calculation):
                print(calculation(a, b))

    def print_guide(self):
        print("-------------------------------------------------\nCommands for Calculator:\n Enter + to sum two numbers\n Enter - to subtract latter number from the first\n Enter * to multiply two numbers\n Enter / to divide first number with the latter\n Enter x to stop\n-------------------------------------------------\n")

    def write(self, thing):
        return print(thing)
