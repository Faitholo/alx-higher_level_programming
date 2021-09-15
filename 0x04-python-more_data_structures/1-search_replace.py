#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return (list(map(lambda x: replace if x is search else x, my_list)))
