def write_file(filename="", text=""):
    with open(filename, 'w', encoding='UTF8') as f:
        num_char = f.write(text)
    return num_char
