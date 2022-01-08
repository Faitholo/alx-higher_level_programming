#!/usr/bin/python3
"""
   function that finds a peak in a list of unsorted integers
"""


def find_peak(list_of_integers):
    """
        This function will find a peak.
    """
    if list_of_integers is None:
        return None
    if len(list_of_integers) == 0:
        return None

        return find_peak(list_of_integers[midpoint:])
