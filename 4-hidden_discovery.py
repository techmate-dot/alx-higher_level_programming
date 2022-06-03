#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    for cont in dir(hidden_4):
        if cont[0] != '_':
            print(cont)
