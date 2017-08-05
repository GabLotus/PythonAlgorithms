import sys

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		n_minus_one = 1
		n_minus_two = 0
		fib = 0
		for i in range(n):
			fib = n_minus_one + n_minus_two
			n_minus_two = n_minus_one
			n_minus_one = fib
		
		return fib
		
		
if len(sys.argv) < 1:
	n = 8
else:
	n = int(sys.argv[1])
	
print(str(fib(n)))
		