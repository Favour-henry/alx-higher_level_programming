#!/usr/bin/python3
# 3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """Prints all integers of a list, in reverse order."""
    if my_list is None:
        return
    for i in reversed(my_list):
        print ('{:d}'format(i))
