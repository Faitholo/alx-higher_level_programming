#!/usr/bin/python3
class MyInt(int):
    def __init__(self, value):
        self.num = value

    def __eq__(self, other):
        return self.num != other

    def __ne__(self, other):
        return self.num == other
