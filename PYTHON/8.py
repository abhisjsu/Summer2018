'''
Level 2

Question:
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
Suppose the following input is supplied to the program:
without,hello,bag,world
Then, the output should be:
bag,hello,without,world
'''


def sortInput(values):
	print(",".join(values));
	values.sort();
	print(",".join(values));


if(__name__=="__main__"):
	val = "without,hello,bag,world".split(',');
	sortInput(val);