import sys
import random

s = [1, 3 ,2 ,9 , 0 , 12, 123 , 43, 17]
og = s

if len(sys.argv) < 2:
	print("insuficient arguments, runing algorithm using array: " + str(s) )
else:
	s = list(sys.argv[1])
	
x = 0
counter = 0
s_sorted = False
while(not s_sorted):
	
	
	x = random.randint(0, len(s)-1)
	y = random.randint(0, len(s)-1)
	s[x], s[y] = s[y], s[x]
		

	
	counter += 1
	print(s)
	s_sorted = True
	for i in range(len(s) - 1):
		if s[i] > s[i+1]:
			s_sorted = False
			
print("It took " + str(counter) + " attempts to sort: " + str(og) + " into: " + str(s) + " try running it again :)")
	