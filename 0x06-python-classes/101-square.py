#!/usr/bin/python3
class Square():
    '''
        Defining a Square
    '''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialization of instance attributes
            Args:
            size (int): Zero or positve number.
        '''
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        '''Updating the private attributes
            Args:
            value (int): tuple of two positve numbers.
        '''
        if isinstance(value, tuple) and len(value) == 2:
                if isinstance(value[0], int) and isinstance(value[1], int):
                    if value[0] >= 0 and value[1] >= 0:
                        self.__position = value
                        return
        raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        '''
            prints in stdout the square with the character # or a new line
            is size is zero.
        '''
        if self.__size == 0:
            return ""

        for line in range(self.__position[1]):
                print()
        for col in range(self.__size - 1):
            print("{}{}".format(" " * self.__position[0], "#" * self.__size))
        return "{}{}".format(" " * self.__position[0], "#" * self.__size)

    def __str__(self):
        return self.my_print()
