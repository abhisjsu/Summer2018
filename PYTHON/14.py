'''
Question 14
Level 2

Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9
'''



inputVal = 'Hello world! 123'
output = {};
output["UPPER"] = 0
output["LOWER"] = 0

for x in inputVal:
	if(x.isupper()):
		output["UPPER"] = output["UPPER"] + 1;
	elif(x.islower()):
		output["LOWER"] = output["LOWER"] + 1;

print("UPPER "+str(output["UPPER"]));
print("LOWER "+str(output["LOWER"]));