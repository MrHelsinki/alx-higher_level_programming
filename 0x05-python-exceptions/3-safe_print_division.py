#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        n = a / b
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result:{:d}".format(n))
        return n
