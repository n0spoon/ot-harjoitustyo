#from iface import *
#import index

class CalculatorService:
    def __init__(self):
        self._calculations = 0

    def isFloat(self,value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def sumService(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        sum = (a+b)
        if int(sum):
            sum = int(a+b)
        self._calculations+=1
        return print(f"{a} + {b} = {sum}")
    
    def subService(self):
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        sub = (a-b)
        if int(sub):
            sub = int(a-b)
        self._calculations+=1
        return print(f"{a} - {b} = {sub}")

    def calculations(self):
        return self._calculations 