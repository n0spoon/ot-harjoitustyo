#from iface import *
#import index

class CalculatorService:
    def __init__(self):
        self._calculations = 0

    def simpleSum(self,a,b):
        return a+b

    def sumService(self,a,b):
        sum = (a+b)
        if int(sum):
            sum = int(a+b)
        self._calculations+=1
        return print(f"{a} + {b} = {sum}")
    
    def subService(self,a,b):
        sub = (a-b)
        if int(sub):
            sub = int(a-b)
        self._calculations+=1
        return print(f"{a} - {b} = {sub}")

    def calculations(self):
        return self._calculations 