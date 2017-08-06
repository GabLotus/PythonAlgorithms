import sys

def fib(n):
	previousCalls = {}
	
	if n == 1:
		return 1
	elif n == 0:
		return 0
	elif n in previousCalls:
		return previousCalls[n]
	else:
		previousCalls[n] = fib(n-1) + fib(n-2)
		return  previousCalls[n]

		
		
n = 0
		
if len(sys.argv) < 2:
	n = 8
else:
	n = int(sys.argv[1])
	
print(str(fib(n)))