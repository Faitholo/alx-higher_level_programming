#!/usr/bin/python3
"""
Defines: class Rectangle
Creates a Rectangle object height and width and calculates its area,
perimeter and prints it with #
"""


class Rectangle:
    """Represents a Rectangle width and height
    """
    def __init__(self, width=0, height=0):
        """Initializes a rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Private instance attribute __width
        """
        return self.__width

    @property
    def height(self):
        """rectangle height
        Returns private instance attribute __height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """set of rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * self.__width + 2 * self.__height

    def __str__(self):
        """Returns string
        """
        rep_str = ""
        if self.__width != 0 and self.__height != 0:
            rep_str += "\n".join("#" * self.__width
                for i in range(self.__height))
        return rep_str
