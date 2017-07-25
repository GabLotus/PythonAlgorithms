import sys



s = "abcddef"

if len(sys.argv) > 1:
	s = sys.argv[1]
else:
	print("Insuficient arguments, testing algorithm with string: " + s)


hashTable = {}

isUniqueCharacters = True

for c in s:
	if c not in hashTable:
		hashTable[c] = 1
	else:
		isUniqueCharacters = False
		break

print(isUniqueCharacters)

	