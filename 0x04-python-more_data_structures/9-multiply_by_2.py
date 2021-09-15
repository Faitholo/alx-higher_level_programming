#!/usr/bin/python3
def multiply_by_2(my_dict):
    tmp_dict = my_dict.copy()
    for x in tmp_dict.keys():
        tmp_dict[x] *= 2
    return (tmp_dict)
