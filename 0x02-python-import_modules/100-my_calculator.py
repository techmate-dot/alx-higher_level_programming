#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    solve = {'+': add, '-': sub, "*": mul, '/': div}

    length = len(argv)
    if (length - 1) == 3:
        operator = argv[2]

    if (length - 1) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print(1)
    elif operator not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and ")
        print(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        result = solve[operator](a, b)
        print(f"{a} {operator} {b} = {result}")
