from calc_funcs import Calc

if __name__ == "__main__":
    calc = Calc()
    calc.add(2,2, printify=True)
    calc.sub(10,3, printify=True)
    calc.mult(2,3, printify=True)
    calc.div(20,4, printify=True)
    calc.pow(10,2, printify=False)

    calc.print_total()
    calc.clear()
    calc.print_total()
