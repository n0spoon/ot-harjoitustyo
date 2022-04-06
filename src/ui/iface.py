from services.calcservice import CalculatorService

class IO:
    def __init__(self):
        self.calculator = CalculatorService()
        self._commands = {
            "+": self.calculator.sumService,
            "-": self.calculator.subService,
        }

    def start(self):
        self.print_guide()
        while True:
            command = input("Enter command: ")
            if command == "x":
                break
            if command not in self._commands:
                self.write("False Command")
                self.print_guide()
                continue
            a = input("Enter first number: ")
            b = input("Enter second number: ")
            calculation = self._commands[command]
            if callable(calculation):
                print(calculation(a,b))

    def print_guide(self):
        print("Commands for Calculator:\nEnter + to sum two numbers\nEnter - to subtract latter number from the first\nEnter x to stop")

#    def read(self,command):
#        return input("Enter command:")
    
    def write(self,thing):
        return print(thing)