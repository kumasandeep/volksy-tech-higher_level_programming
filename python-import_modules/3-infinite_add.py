#!/usr/bin/python3
if _name_ == "__main__":
    import sys
    sum = 0
    for i in range(1, len(sys.argv)):
        sum = sum + int(sys.argv[i])
    print(sum)
