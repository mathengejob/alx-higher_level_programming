#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    argv = argv[1:]
    total = 0
    for i in argv:
        y = int(i)
        total = total + y
    print("{:d}".format(total))
