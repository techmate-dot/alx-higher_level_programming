#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lists = sys.argv
    length = len(sys.argv)
    sum = 0
    for i in range(1, length):
        sum += int(lists[i])
print(sum)
