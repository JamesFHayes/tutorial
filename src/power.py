"""This is a Script that calculates one number to the power of another."""

import sys
import math

def to_the_power(x, y = 2):
    """ trying this out
    """
    return x ** y

def square_root(x):
    return math.sqrt(x)
	
if len(sys.argv) < 3:
	print("You must supply 2 parameters!")
	exit()

x = int(sys.argv[1])
y = int(sys.argv[2]) 
print("{0} to the power of {1} is {2}".format(x, y, to_the_power(x, y)))
print("The square root of {0} is {1}".format(x, square_root(x)))
