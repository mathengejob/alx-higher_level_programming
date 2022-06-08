#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]

    if len(argv) < 3 or len(argv) > 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        print("{:d}".format(1))
    elif argv[1] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        print("{:d}".format(1))
    else:
        a = int(argv[0])
        b = int(argv[2])
        if argv[1] == "+":
            print("{:d}".format(a + b))
        if argv[1] == "-":
            print("{:d}".format(a - b))
        if argv[1] == "*":
            print("{:d}".format(a * b))
        if argv[1] == "/":
            printi("{:d}".format(a / b))
