#!/usr/bin/python3
def print_last_digit(number):
    exe = 0
    if number < 0:
        number *= -1
    exe = 1
    last = number % 10
    if exe == 1:
        number *= -1
    print("{:d}".format(last), end="")
    return last
