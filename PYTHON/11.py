'''
Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers 
as its input and then check whether they are divisible by 5 or not. 
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.
'''

outputList = []

def getOutput(val):
	#converting the binary string into decimal integer
	intval = int(val,2)
	if(intval % 5 == 0):
		outputList.append(str(val))
	

if(__name__=="__main__"):
	values = '0100,0011,1010,1001'.split(',')
	for val in values:
		getOutput(val)

	print(",".join(outputList))