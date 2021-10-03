#!/usr/bin/python3
class Square():
    '''
        Defining a Square
    '''

    def __init__(self, size=0):
        '''Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculates the area

            Return: The current square area.
        '''
        return self.__size * self.__size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Updating the private attributes
            Args:
            value (int): Zero or positve number.
        '''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        '''
            prints in stdout the square with the character # or a new line
            is size is zero.
        '''
        if self.__size == 0:
            print()
            return
        for col in range(self.__size):
            for row in range(self.size):
                print("#", end="")
            print()
