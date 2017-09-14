"""This is a Script that calculates one number to the power of another."""
def to the power(x, y = 2):
	result = x
	for i in range(0, y):
		result = result * x
	return result
	
x = 9
y = 8
print("{0} to the power of {2} is: ".format(x, y, to the power(x, y)))
