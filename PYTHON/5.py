'''
Question:
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class StringOperations:

	def __init__(self,inputString):
		self.inputString = inputString;

	def setString(self,x):
		self.inputString = x;

	def printString(self):
		print("The string content is "+self.inputString);

s1 = StringOperations("Hello");
print(s1.inputString);

s1.setString("World");

print(s1.inputString);