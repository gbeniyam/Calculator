from calc_funcs import Calc

if __name__ == "__main__":
    calc = Calc()
    calc.add(2.5,4.0)
    calc.sub(10,3)
    calc.mult(2,3)
    calc.div(20,4)
    calc.pow(10,2)

    calc.print_total()
    calc.clear()
    calc.print_total()
