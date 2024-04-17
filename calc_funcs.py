class Calc:
    def __init__(self) -> None:
        total = 0

    def add(self, x, y):
        return x + y
    
    def sub(self, x, y):
        return x - y
    
    def mult(self, x, y):
        return x * y
    
    def div(self, x, y):
        if y != 0:
            return x / y
        else:
            print("Error: Division by 0")
            return None
    def pow(self, x, y):
        return x ** y

    def clear(self):
        self.total = 0
