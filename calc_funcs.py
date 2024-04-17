class Calc:
    def __init__(self) -> None:
        self.total = 0

    def add(self, x, y, printify=False):
        self.total = x + y
        if printify:
            print(f"{x} + {y} = {self.total}")
        # print out the result if desired.

    def sub(self, x, y, printify=False):
        self.total = x - y
        if printify:
            print(f"{x} - {y} = {self.total}")

    def mult(self, x, y, printify=False):
        self.total = x * y
        if printify:
            print(f"{x} * {y} = {self.total}")

    def div(self, x, y, printify=False):
        if y != 0:
            self.total = x / y
            if printify:
                print(f"{x} / {y} = {self.total}")
        else:
            print("Error: Division by 0")
            return None

    def pow(self, x, y, printify=False):
        if printify:
            self.total = x ** y

    def print_total(self):
        print(f"Current total: {self.total}")

    def clear(self):
        self.total = 0

"""
1. def print, print statement. abstract for a class
2. TODO: func for taking sum, and output to a file
3. find a FreeAPI endpoint that I could hit, get json data.
    a. thecocktaildb
"""
