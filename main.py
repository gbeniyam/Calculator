from calc_funcs import Calc

if __name__ == "__main__":
    calc = Calc()
    sum = calc.add(2,2)
    sub = calc.sub(10,3)
    mult = calc.mult(2,3)
    div = calc.div(20,4)
    pow = calc.pow(10,2)

    print(f"sum 2+2: {sum}")
    print(f"sub 10-3: {sub}")
    print(f"mult 2*3: {mult}")
    print(f"div 20/4: {div}")
    print(f"pow 10^2: {pow}")
