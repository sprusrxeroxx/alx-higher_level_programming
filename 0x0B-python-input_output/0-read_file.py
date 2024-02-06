#!/usr/bin/python3
'''A function to read a text file and print out to  stdout'''

def read_file(filename=""):
    '''A representation of a file read function'''
    with open(filename,"r", encoding='utf8') as fd:
        for line in fd:
            print(line)
