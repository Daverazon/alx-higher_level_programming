#!/usr/bin/python3
if (__name__ == "__main__"):
    from calculator_1 import add, sub, mul, div
    import sys
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    func = (add, sub, mul, div)
    op = ['+', '-', '*', '/']
    for sign in op:
        if sign == sys.argv[2]:
            print("{:d} {} {:d} = {:d}\
".format(a, sys.argv[2], b, func[op.index(sign)](a, b)))
    if sys.argv[2] not in op:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
