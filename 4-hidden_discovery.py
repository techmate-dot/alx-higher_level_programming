#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for cont in dir(hidden_4):
        if cont[0] != '_':
            print(cont)
