from enum import Enum

class Print_Out(Enum):
    No_Output = 0
    Standard_Out = 1
    File_Out = 2

class Calc:
    def __init__(self) -> None:
        self.total = 0

    def add(self, x: int | float, y: int | float, printify=Print_Out.Standard_Out):
        self.total = x + y
        if printify == Print_Out.Standard_Out:
            print(f"{x} + {y} = {self.total}")
        elif printify == Print_Out.File_Out:
            with open("Calc_output.txt", "a") as f:
                f.write(f"{x} + {y} = {self.total}\n")

    def sub(self, x: int | float, y: int | float, printify=Print_Out.No_Output):
        self.total = x - y
        if printify == Print_Out.Standard_Out:
            print(f"{x} - {y} = {self.total}")
        elif printify == Print_Out.File_Out:
            with open("Calc_output.txt", "a") as f:
                f.write(f"{x} - {y} = {self.total}\n")

    def mult(self, x: int | float, y: int | float, printify=Print_Out.File_Out):
        self.total = x * y
        if printify == Print_Out.Standard_Out:
            print(f"{x} * {y} = {self.total}")
        elif printify == Print_Out.File_Out:
            with open("Calc_output.txt", "a") as f:
                f.write(f"{x} * {y} = {self.total}\n")

    def div(self, x: int | float, y: int | float, printify=Print_Out.File_Out):
        if y != 0:
            self.total = x / y
            if printify == Print_Out.Standard_Out:
                print(f"{x} / {y} = {self.total}")
            elif printify == Print_Out.File_Out:
                with open("Calc_output.txt", "a") as f:
                    f.write(f"{x} / {y} = {self.total}\n")
        else:
            print("Error: Division by 0")
            return None

    def pow(self, x: int | float, y: int | float, printify=Print_Out.File_Out):
        if printify == Print_Out.Standard_Out:
            print(f"{x} ^ {y} = {self.total}")
        elif printify == Print_Out.File_Out:
            with open("Calc_output.txt", "a") as f:
                f.write(f"{x} ^ {y} = {self.total}\n")

    def print_total(self):
        print(f"Current total: {self.total}")

    def clear(self):
        self.total = 0

"""
1. def print, print statement. abstract for a class
2. func for taking sum, and output to a file
3. TODO: find a FreeAPI endpoint that I could hit, get json data.
    a. thecocktaildb
"""
