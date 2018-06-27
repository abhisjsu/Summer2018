
'''
Question:
Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.

'''

def printMultiples(input):
	output = []
	for i in range(1,input+1):
		if (i%7==0 and i%5!=0):
			output.append(str(i))
	print(",".join(output));

if (__name__=="__main__"):
	printMultiples(50);

'''
Join function in Python: 
	It is used to join the multiples elements in a collection by come delimiter
		delimiter.join(collection)
'''