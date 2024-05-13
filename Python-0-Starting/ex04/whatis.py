import sys

if len(sys.argv) > 1:
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument is provided")
    elif sys.argv[1].isdigit():
        if  int(sys.argv[1]) % 2 == 0:
            print("I'm Even")
        elif int(sys.argv[1]) % 2 != 0:
            print("I'm Odd")
    else:
        print("AssertionError: argument is not an integer")




# They are actually 3 most common ways to get the args
# 1.sys.argv 2.getopt module 3.argparse module
# resource:
# - https://www.geeksforgeeks.org/command-line-arguments-in-python/