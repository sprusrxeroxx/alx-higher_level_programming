#!/usr/bin/python3
'''A function to read a text file and print out to  stdout'''


def write_file(filename="", text=""):
    '''A representation of a file write function

    Args:
        filename: A string to capture the name of the file
        text: The string the user wants to write

    Returns:
        Writes to a file
    '''

    with open(filename, "w", encoding='UTF-8') as fd:
        fd.write(text)
    return len(text)
