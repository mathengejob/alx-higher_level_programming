#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    args_count = len(argv)
    if args_count > 1:
        i = 1
        print("{:d} arguments:".format(args_count))
        for i in range(args_count):
            print("{:d}: {:s}".format(i, argv[i]))
    elif args_count == 1:
        print("{:d} argument:".format(args_count))
        print("{:d}: {:s}".format(1, argv[0]))
    else:
        print("{:d} arguments.".format(args_count))
