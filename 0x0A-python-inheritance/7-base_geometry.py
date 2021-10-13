#!/usr/bin/python3
'''
    Implementing a Geometry class
'''


class BaseGeometry:
    def area(self):
        '''
            Calculating the area
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''
            Validating the integer
        '''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
