import sys
import os

def fib(n):
	percentage_complete = 0
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		n_minus_one = 1
		n_minus_two = 0
		fib = 0
		for i in range(n):
			if (i/n)*100 > percentage_complete:
				percentage_complete += 1
				sys.stdout.write(str(percentage_complete) + "\r")
			fib = n_minus_one + n_minus_two
			n_minus_two = n_minus_one
			n_minus_one = fib
		
		return fib
		
		
if len(sys.argv) < 2:
	n = 8
else:
	n = int(sys.argv[1])
	
print(str(fib(n)))
		