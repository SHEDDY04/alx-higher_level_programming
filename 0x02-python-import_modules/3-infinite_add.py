#!/usr/bin/python3

if __name__ == "__main__":
    """print the sum of all arguments."""
    import sys

    total = 0
    for i in range(len(sys.argv) - 1):
        total += int(sysargv[i + 1])
        print("{}".format(total))
