class calculator:
    
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
        
    def add(self):
        return self.number1 + self.number2
    
    def sub(self):
        return self.number1 - self.number2
    
    def divide(self):
        try:
            return self.number1 / self.number2
        except ZeroDivisionError:
            return "Cannot be divided by zero"
        
    def multiply(self):
        return self.number1 * self.number2
    
calculate = calculator(1, 0)
print(calculate.divide())