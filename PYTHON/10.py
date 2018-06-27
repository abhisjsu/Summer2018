'''
Question:
Write a program that accepts a sequence of whitespace separated words as input and 
prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world
'''

def removeDuplicateAndSort(values):
	print(values);
	values = list(set(values.split(' ')));
	print(' '.join(values));
	values.sort();
	print(' '.join(values));


if(__name__=="__main__"):
	removeDuplicateAndSort('hello world and practice makes perfect and hello world again');

'''
Output:
hello world and practice makes perfect and hello world again
makes and world again perfect practice hello
again and hello makes perfect practice world
'''