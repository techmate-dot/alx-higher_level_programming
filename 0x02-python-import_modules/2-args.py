#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    lists = sys.argv
    length = len(sys.argv)
    if length == 1:
        print(f"{length - 1} arguments.")
    else:
        print(f"{length - 1} {'argument' if length == 2 else 'arguments'}:")
    for i in range(1, length):
        print(f"{i}: {lists[i]}")
