#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):

    index = printed_ints = 0
    while True:
        try:
            if index < x:
                print("{:d}".format(my_list[index]), end='')
                index += 1
                printed_ints += 1
            else:
                print()
                return printed_ints
        except (ValueError, TypeError):
            index += 1
