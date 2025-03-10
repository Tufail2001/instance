class Calculator:
    def __init__(self):
        self.result = 0
        self.history = []

    def add(self, a, b=None):
        if b is None:
            self.result += a
        else:
            self.result = a + b
        self.history.append(f"Added: {a} {'' if b is None else f'+ {b}'} = {self.result}")
        return self.result

    def subtract(self, a, b=None):
        if b is None:
            self.result -= a
        else:
            self.result = a - b
        self.history.append(f"Subtracted: {a} {'' if b is None else f'- {b}'} = {self.result}")
        return self.result

    def multiply(self, a, b=None):
        if b is None:
            self.result *= a
        else:
            self.result = a * b
        self.history.append(f"Multiplied: {a} {'' if b is None else f'* {b}'} = {self.result}")
        return self.result

    def divide(self, a, b=None):
        try:
            if b is None:
                if a == 0:
                    raise ZeroDivisionError
                self.result /= a
            else:
                if b == 0:
                    raise ZeroDivisionError
                self.result = a / b
            self.history.append(f"Divided: {a} {'' if b is None else f'/ {b}'} = {self.result}")
            return self.result
        except ZeroDivisionError:
            return "Error: Division by zero"

    def power(self, a, b=None):
        if b is None:
            self.result **= a
        else:
            self.result = a ** b
        self.history.append(f"Power: {a} {'' if b is None else f'^ {b}'} = {self.result}")
        return self.result

    def clear(self):
        self.result = 0
        return self.result

    def get_history(self):
        return self.history

    def get_result(self):
        return self.result
    

    calc = Calculator()
    calc.add(5, 3)      # Returns 8
    calc.multiply(2)     # Returns 16
    calc.subtract(5)     # Returns 11
    calc.divide(2)       # Returns 5.5
    calc.power(2)        # Returns 30.25
    calc.get_history()   # Returns list of all operations