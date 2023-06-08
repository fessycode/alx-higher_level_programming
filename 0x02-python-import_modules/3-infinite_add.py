#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    count = len(argv)
    index = 1
    res = 0
    while index <= count:
        res += int(sys.argv[index])
        index += 1
    print("{:d}".format(res))
