#!/usr/bin/python3
if (__name__ == "__main__"):
    import calculator_1
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    for sign in ('+', '-', '*', '/'):
        if sign == argv[2]:
            print("{} {} {} = {}".format(argv[1], argv[2],\
                    argv[3], eval(f"{argv[1]} {argv[2]} {argv[3]}"))
        else:
            print("Unknown operator. Available operators:"
                " +, -, * and /")
            exit(1)
