from .__init__ import *
import random

def primecheckFunc():
	n = random.randint(0,99999)
	problem = "Is the given number {} is prime or composite?".format(n)
	if (n <= 1):
		solution = "neither Prime nor Composite"
	elif (n <= 3):
		solution = "Prime"

	elif (n % 2 == 0 or n % 3 == 0):
		solution = "Composite"
	else:
		i = 5
		while(i * i <= n) : 
			if (n % i == 0 or n % (i + 2) == 0) : 
				solution = "Composite"
				break
			i = i + 6
		solution = "Prime"

	return problem, solution