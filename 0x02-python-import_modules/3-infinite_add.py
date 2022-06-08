#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    if len(argv) > 1:
        total = 0
        for i in argv:
            y = int(i, base=10)
            total = total + y
        print("{:d}".format(total))
