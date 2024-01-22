#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in my_list[:x]:
            print(i, end="")
            n += 1
        print("\n", end="")
    except IndexError:
        print("x higher than loop")

    return n
