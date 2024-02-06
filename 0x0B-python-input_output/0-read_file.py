#!/usr/bin/python3
'''A function to read a text file and print out to  stdout'''


def read_file(filename=""):
    '''A representation of a file read function

    Args:
        filename: A string to capture the name of the file

    Returns:
        prints Contents of file to the screen
    '''
    with open(filename, "r", encoding='UTF-8') as fd:
        for line in fd:
            print(line)
