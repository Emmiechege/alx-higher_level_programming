#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of arguments and
    the lists of its arguments
    """
    import sys

    list_args = sys.argv
    len_args = len(list_args) - 1

    if len_args == 0:
        print(len_args, "arguments.")
    elif len_args == 1:
        print(len_args, "arguments:")
        for z in range(len_args + 1):
            print("{:d}: {}".format(z, list_args[z]))
    elif len_args > 1:
        print(len_args, "arguments:")
        for k in range(1, len_args + 1):
            print("{:d}: {}".format(k, list_args[k]))
