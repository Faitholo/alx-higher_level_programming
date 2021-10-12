#!/usr/bin/python3
''' function that returns the number of lines of a text file
'''


def number_of_lines(filename=""):
    ''' function: number_of_lines
    '''
    if filename == "" or type(filename) != str:
        return 0
    counter = 0
    with open(filename, 'r') as f:
        for line in f:
            counter += 1
    return counter
