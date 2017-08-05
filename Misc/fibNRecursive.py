import sys

def fib(n):
	if n == 1:
		return 1
	elif n == 0:
		return 0
	else:
		return fib(n-1) + fib(n-2)

		
		
n = 0
		
if len(sys.argv) < 1:
	n = 8
else:
	n = int(sys.argv[1])
	
print(str(fib(n)))