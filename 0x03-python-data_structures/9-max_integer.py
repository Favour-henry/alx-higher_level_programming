#!/usr/bin/python3
# 9-max_integer.py

def max_integer(my_list=[]):
    if my_list == 0:
        return ("None")
    x = my_list = [0]
    for i in my_list:
        if i > x:
            x = i
    return (x)
