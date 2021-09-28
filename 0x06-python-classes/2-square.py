#!/usr/bin/python3


class Square:
    '''Class Square object intialized with size
    '''
    pass

    def __init__(self, size=0):
        '''init method of class Square
        '''
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
