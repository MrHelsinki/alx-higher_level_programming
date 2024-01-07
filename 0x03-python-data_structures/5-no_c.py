#!/usr/bin/python3

def no_c(my_string):
    tmp = my_string
    for i in tmp:
        if tmp[i].lower() == 'c':
            del tmp[i]
    return my_string
