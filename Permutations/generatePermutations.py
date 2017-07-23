import sys

def insertCharacters(s, c):
	strings = []
	
	for x in range(0, len(s) +  1):
		sc_permutation = s[0:x] + c + s[x:len(s)]
		strings.append(sc_permutation)
		
	return strings
		


def findAllPermutations(s):
	permutations = []
	permutations.append("")
	
	for c in s:
		tempPermutations = []
		for p in permutations:
			insertedChars = insertCharacters(p, c)
			for p_temp in insertedChars:
				tempPermutations.append(p_temp)
		
		permutations = tempPermutations
	return permutations

# new_s = insertCharacters(s[0:(len(s) - 1)], s[(len(s) - 1)])
s = sys.argv[1]

new_s = findAllPermutations(s)
print(new_s)