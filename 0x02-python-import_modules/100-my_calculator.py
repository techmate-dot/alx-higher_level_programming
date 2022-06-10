#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    from calculator_1 import add, sub, mul, div

    solve = {'+': add, '-': sub, '*': mul, '/': div}
    operators = "*+/-*"

    length = len(argv)
    if (length) == 4:
        operator = argv[2]

    if (length) != 4:
        print(f"Usage: {argv[0]} <a> <operator> <b>")
        exit(1)
    elif operator not in operators:
        print("Unknown operator. Available operators: +, -, * and ")
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        result = solve[operator](a, b)
        if operator == '*':
             print("{:d} {:s} {:d} = {:d}".format(a, operator, b, mul(a, b)))
        else:
            print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
