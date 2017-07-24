import sys

s = "abcdef"
d = "bdfhj"

if len(sys.argv) >= 3:
	s = sys.argv[1]
	d = sys.argv[2]
else:
	print("Insuficient arguments, running algorithm with strings: " + s + " and: " + d + " instead.")



hashTable = {}

for c in d:
	hashTable[c] = True
	
for c in s:
	if c in hashTable:
		print(c + ": True")
	else:
		print(c + ": False")