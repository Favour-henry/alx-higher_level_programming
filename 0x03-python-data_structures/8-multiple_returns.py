#!/usr/bin/python3
# 8-multiple_returns.py

def multiple_returns(sentence):
    length = len(sentence)
    first_char = sentence[0] if length > 0 else "None"
    tup = length, first_char
    return(tup)
