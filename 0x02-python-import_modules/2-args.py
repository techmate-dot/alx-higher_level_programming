#!/usr/bin/python3
import sys
lists = sys.argv
length = len(sys.argv)
print(f"{length - 1} arguments:")
for i in range(1, length):
    print(f"{i}: {lists[i]}")
