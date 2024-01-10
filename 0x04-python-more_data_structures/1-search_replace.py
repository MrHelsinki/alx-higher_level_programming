#!/usr/bin/python3

def search_replace(my_list, search, replace):
    cp = []
    for i in my_list:
        if i == search:
            replace.append(cp)
        else:
            i.append(cp)
    return cp
