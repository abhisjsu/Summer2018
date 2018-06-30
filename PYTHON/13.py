'''
Question 13
Level 2

Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3
'''


# using isdigit and isalpha on a datatype

inputVal = 'hello world! 123'
output = {};
output["LETTERS"] = 0
output["DIGITS"] = 0

for x in inputVal:
	if(x.isdigit()):
		output["DIGITS"] = output["DIGITS"] + 1;
	elif(x.isalpha()):
		output["LETTERS"] = output["LETTERS"] + 1;

print("LETTERS "+str(output["LETTERS"]));
print("DIGITS "+str(output["DIGITS"]));