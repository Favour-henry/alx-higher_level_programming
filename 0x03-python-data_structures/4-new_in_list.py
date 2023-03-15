#!/usr/bin/python3
# 4-new_in_list.py

def new_in_list(my_list, idx, element):
    """ Replaces an element in a list at a specific position without modifying the original list"""
    tmp_list = my_list[:]
    if 0 <= idx < (len(my_list):
            tmp_list[idx] = element
            return (tmp_list)
    return (my_list)
