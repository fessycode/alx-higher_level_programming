#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argv_count = len(argv)
    if argv_count == 1:
        print("{:d} arguments.".format(argv_count - 1))
    elif argv_count == 2:
        print("{:d} argument:".format(argv_count - 1))
        index = 1
        while index < argv_count:
            print("{}: {}".format(index, argv[index]))
            index += 1
    else:
        print("{:d} arguments:".format(argv_count - 1))
        index = 1
        while index < argv_count:
            print("{}: {}".format(index, sys.argv[index]))
            index += 1
