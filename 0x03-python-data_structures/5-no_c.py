#!/usr/bin/python3

def no_c(my_string):
    tmp = my_string
    result = []

    for i in tmp:
        if not i.lower() == 'c':
            result.append(i)
    return ''.join(result)
