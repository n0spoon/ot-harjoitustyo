class CalculationRepository:
    def __init__(self):
        self._calculations = []

    def add_calculation(self, content):
        self._calculations.append(content)

    def print_calculations(self):
        return print(self._calculations)

    def count_calculations(self):
        return len(self._calculations)
