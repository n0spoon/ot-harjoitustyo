class CalculatorService:
    def __init__(self):
        self._calculations = []

    def stringToNumber(self,s):
        try:
            return int(str(s),0)
        except:
            return float(s)

    def simpleSum(self,a,b):
        a = self.stringToNumber(a)
        b = self.stringToNumber(b)
        return a+b

    def sumService(self,a,b):
        a = self.stringToNumber(a)
        b = self.stringToNumber(b)
        sum = (a+b)
        pieces = str(sum).split(".")
        if len(pieces[-1]) == 1: 
            last = int(pieces[-1])
            if last == 0:
                sum = int(sum)
        self._calculations.append(sum)
        return f"{a} + {b} = {sum}"

    
    def subService(self,a,b):
        a = self.stringToNumber(a)
        b = self.stringToNumber(b)
        sub = (a-b)
        pieces = str(sub).split(".")
        if len(pieces[-1]) == 1: 
            last = int(pieces[-1])
            if last == 0:
                sub = int(sub)
        self._calculations.append(sub)
        return f"{a} - {b} = {sub}"

    def calculations(self):
        return len(self._calculations)