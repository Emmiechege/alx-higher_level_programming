#!/usr/bib/python3

def is_same_class(obj, a_class):
    """Checks if object is exactly an instance of the specified class
    Returns true if it is
    Returns false otherwise
    """
    return type(obj) is a_class
