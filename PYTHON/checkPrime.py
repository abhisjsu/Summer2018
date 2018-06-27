'''
Program to print all prime numbers from 1 to 100
'''


def checkPrime(x):
	for i in range(2,x):
		if(x%i==0):
			return False
	return True

output = []

for i in range(2,100):
	if(checkPrime(i)):
		output.append(str(i))

print ",".join(output)