#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx > 0:
        return None
    if idx >= len(my_list):
        return None
    tmp = my_list
    tmp[idx] = element
    return tmp
