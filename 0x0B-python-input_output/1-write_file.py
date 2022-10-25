#!/usr/bin/python3
""" Module that contains a function that appends to a text file
"""

def write_file(filename="", text=""):
    """ Function that appends to a text file

    Args:
        filename: filename
        text: text to write

    Raises
        Exception: when the file can be opened

    """
    with open(filename, 'w', encoding="utf-8") as f:
        lines = f.write(text)
    with open(filename, encoding="utf-8") as f:
        charnum = 0
        while True:
            line = f.readline()
            if not line:
                break
            for word in line.split():
                for char in word:
                    charnum += 1
        return charnum
