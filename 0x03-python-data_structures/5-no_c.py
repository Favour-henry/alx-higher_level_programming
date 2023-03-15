#!/usr/bin/python3
# 5-no_c.py

def no_c(my_string):
    '''Removes all characters c and C'''
    for i in my_string:
        if (i != 'c') and (i != 'C'):
           new_str += i
        return (new_str)
