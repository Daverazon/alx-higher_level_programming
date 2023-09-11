#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    func = [add, sub, mul, div]
    op = ('+', '-', '*', '/')
    for sign in op:
        if sign == argv[2]:
            print("{:d} {} {:d} = {:d}\
                    ".format(a, argv[2], b, func[op.index(sign)](a, b)))
    if argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
