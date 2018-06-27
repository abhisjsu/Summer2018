'''
Question:
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
8
Then, the output should be:
40320

	This program calculates the factorial of a number through two menthods
		1. Recursive method 
		2. Iterative method
'''
def calculateFactorial(input):
	if(input==1):
		return 1;
	else:
		return input*calculateFactorial(input-1);

def interativeFactorial(input):
	result = 1;
	if(input == 1):
		return result;
	else:
		for i in range(1,input+1):
			result= result*i;
		return result;

if(__name__=="__main__"):
	x = calculateFactorial(8);
	print(x);
	x = interativeFactorial(8);
	print(x);

