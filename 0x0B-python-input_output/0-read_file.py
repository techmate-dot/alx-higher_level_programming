def read_file(filename=""):
    with open(filename, 'r', encoding='UTF8') as f:
        value = f.read()
    print(value)
