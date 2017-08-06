import sys

def fib(n, previousCalls):
	
	
	if n == 1:
		return 1
	elif n == 0:
		return 0
	elif n in previousCalls:
		
		return previousCalls[n]
	else:
		previousCalls[n] = fib(n-1, previousCalls) + fib(n-2, previousCalls)
		return  previousCalls[n]

		
		
n = 0
previousCalls = {}
		
if len(sys.argv) < 2:
	n = 8
else:
	n = int(sys.argv[1])
	
print(str(fib(n, previousCalls)))